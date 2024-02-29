// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, prefer_const_literals_to_create_immutables, must_be_immutable, non_constant_identifier_names, avoid_print, prefer_const_constructors_in_immutables, unnecessary_string_interpolations, unnecessary_brace_in_string_interps, library_private_types_in_public_api, duplicate_import
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class MySensorPage extends StatefulWidget {
  @override
  _MySensorPageState createState() => _MySensorPageState();
}

class _MySensorPageState extends State<MySensorPage> {
  String temperature = '';
  String humidity = '';

  Future<void> receiveTemperature(String endpoint) async {
    final url = Uri.parse('http://192.168.126.22:5000/$endpoint');
    try {
      final response = await http.get(url);
      print(response.statusCode);
      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        final statusCode = responseData['status_code'];
        final receivedTemperature = responseData['data']['temperature'];

        print('Status Code: $statusCode');
        print('Temperature: $receivedTemperature');

        setState(() {
          temperature = receivedTemperature;
        });
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error sending request: $e');
    }
  }

  Future<void> receiveHumidity(String endpoint) async {
    final url = Uri.parse('http://192.168.126.22:5000/$endpoint');
    try {
      final response = await http.get(url);
      print(response.statusCode);
      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        final statusCode = responseData['status_code'];
        final receivedHumidity = responseData['data']['humidity'];

        print('Status Code: $statusCode');
        print('Humidity: $receivedHumidity');

        setState(() {
          humidity = receivedHumidity;
        });
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error sending request: $e');
    }
  }

  void getTemperature() {
    print('Get Temperature');
    receiveTemperature('temperature');
  }

  void getHumidity() {
    print('Get Humidity');
    receiveHumidity('humidity');
  }

  @override
  Widget build(BuildContext context) {
    return MySensorPageControl(
      getTemperature: () => receiveTemperature('temperature'),
      getHumidity: () => receiveHumidity('humidity'),
      temperature: temperature,
      humidity: humidity,
    );
  }
}

class MySensorPageControl extends StatelessWidget {
  final VoidCallback getTemperature;
  final VoidCallback getHumidity;
  final String temperature;
  final String humidity;

  MySensorPageControl({
    required this.getHumidity,
    required this.getTemperature,
    required this.humidity,
    required this.temperature,
  });

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
            child: Column(
              children: [
                SizedBox(
                  height: 15.0,
                ),
                Row(
                  children: [
                    ElevatedButton(
                      onPressed: () {
                        getTemperature();
                        getHumidity();
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.white, // Background color
                        padding:
                            EdgeInsets.symmetric(horizontal: 20, vertical: 10),

                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(8.0),
                            side: BorderSide(color: Colors.black, width: 1.5)),

                        fixedSize: Size(143, 37),
                      ),
                      child: Text(
                        'Refresh',
                        style: TextStyle(
                          color: Colors.black,
                          fontSize: 20.0,
                          fontFamily: 'regular',
                          fontWeight: FontWeight.bold,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ],
                ),
                SizedBox(
                  height: 20.0,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 100.0,
                      height: 156.0,
                      decoration: BoxDecoration(
                        color: Color(0xFFE1E1E1),
                        borderRadius: BorderRadius.circular(99.0),
                        border: Border.all(
                          color: Colors.black,
                          width: 1.0,
                        ),
                      ),
                      child: Column(
                        children: [
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                width: 90.0,
                                height: 90.0,
                                decoration: BoxDecoration(
                                  color: Colors.white,
                                  borderRadius: BorderRadius.circular(4000.0),
                                  border: Border.all(
                                    color: Colors.black,
                                    width: 1.0,
                                  ),
                                ),
                                child: Center(
                                  child: Image.asset(
                                    'assets/water-drop.png', // Replace 'your_image.png' with your image asset path
                                    width: 68.0, // Set the width of the image
                                    height: 68.0, // Set the height of the image
                                  ),
                                ),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(
                                '$humidity %',
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 20.0,
                                  fontFamily: 'regular',
                                  fontWeight: FontWeight.bold,
                                ),
                                textAlign: TextAlign.center,
                              ),
                            ],
                          ),
                        ],
                      ),
                    )
                  ],
                ),
                SizedBox(
                  height: 15.0,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 100.0,
                      height: 156.0,
                      decoration: BoxDecoration(
                        color: Color(0xFFE1E1E1),
                        borderRadius: BorderRadius.circular(99.0),
                        border: Border.all(
                          color: Colors.black,
                          width: 1.0,
                        ),
                      ),
                      child: Column(
                        children: [
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                width: 90.0,
                                height: 90.0,
                                decoration: BoxDecoration(
                                  color: Colors.white,
                                  borderRadius: BorderRadius.circular(4000.0),
                                  border: Border.all(
                                    color: Colors.black,
                                    width: 1.0,
                                  ),
                                ),
                                child: Center(
                                  child: Image.asset(
                                    'assets/temparature.png', // Replace 'your_image.png' with your image asset path
                                    width: 68.0, // Set the width of the image
                                    height: 68.0, // Set the height of the image
                                  ),
                                ),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(
                                '${temperature} \u00B0C',
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 20.0,
                                  fontFamily: 'regular',
                                  fontWeight: FontWeight.bold,
                                ),
                                textAlign: TextAlign.center,
                              )
                            ],
                          ),
                        ],
                      ),
                    )
                  ],
                ),
                SizedBox(
                  height: 15.0,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 100.0,
                      height: 156.0,
                      decoration: BoxDecoration(
                        color: Color(0xFFE1E1E1),
                        borderRadius: BorderRadius.circular(99.0),
                        border: Border.all(
                          color: Colors.black,
                          width: 1.0,
                        ),
                      ),
                      child: Column(
                        children: [
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                width: 90.0,
                                height: 90.0,
                                decoration: BoxDecoration(
                                  color: Colors.white,
                                  borderRadius: BorderRadius.circular(4000.0),
                                  border: Border.all(
                                    color: Colors.black,
                                    width: 1.0,
                                  ),
                                ),
                                child: Center(
                                  child: Image.asset(
                                    'assets/fire.png', // Replace 'your_image.png' with your image asset path
                                    width: 68.0, // Set the width of the image
                                    height: 68.0, // Set the height of the image
                                  ),
                                ),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 5.0,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(
                                'None',
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 20.0,
                                  fontFamily: 'regular',
                                  fontWeight: FontWeight.bold,
                                ),
                                textAlign: TextAlign.center,
                              ),
                            ],
                          ),
                        ],
                      ),
                    )
                  ],
                ),
                SizedBox(
                  height: 20.0,
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
