// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, prefer_const_literals_to_create_immutables, unused_import

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:webview_flutter/webview_flutter.dart';

class MyAutoPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MyAutoPageControl();
  }
}

class MyAutoPageControl extends StatelessWidget {
  Future<String> fetchWebcamStream() async {
    final response =
        await http.get(Uri.parse('http://192.168.126.22:5000/auto'));

    if (response.statusCode == 200) {
      // Assuming the response contains the webcam stream URL
      return response.body;
    } else {
      throw Exception('Failed to fetch webcam stream');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
            margin: EdgeInsets.only(top: 40.0),
            decoration: BoxDecoration(
              color: Color(0xFFC2E95C),
              border: Border(
                top: BorderSide(
                  color: Colors.black, // Border color
                  width: 1.5, // Border width
                ),
                bottom: BorderSide(
                  color: Colors.black, // Border color
                  width: 1.5, // Border width
                ),
              ),
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(12.0),
                topRight: Radius.circular(12.0),
              ),
            ),
            child: Center(
              child: Column(children: [
                SizedBox(
                  height: 35.0,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      height: 245.84,
                      width: 311.91, // Adjust the height as needed
                      color: Colors.blue,
                      child: Center(
                        child: Image.network(
                          'http://192.168.126.22:5000/auto', // Replace with your actual image URL
                        ),
                      ),
                    ),
                  ],
                ),
                SizedBox(
                  height: 60.0,
                ),
              ]),
            )),
      ),
    );
  }
}
