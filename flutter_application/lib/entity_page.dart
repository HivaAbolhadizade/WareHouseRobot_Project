// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, prefer_const_literals_to_create_immutables, unnecessary_brace_in_string_interps, prefer_const_constructors_in_immutables

import 'package:flutter/material.dart';
import 'package:flutter_application_2/main.dart';

class MyEntityPage extends StatelessWidget {
  final String redValue;
  final String blueValue;
  final String greenValue;

  // Constructor to receive data from Page 1
  MyEntityPage({
    required this.redValue,
    required this.blueValue,
    required this.greenValue,
  });

  @override
  Widget build(BuildContext context) {
    return MyEntityPageControl(
      redValue: redValue,
      blueValue: blueValue,
      greenValue: greenValue,
    );
  }
}

class MyEntityPageControl extends StatelessWidget {
  final String redValue;
  final String blueValue;
  final String greenValue;

  // Constructor to receive data from Page 1
  MyEntityPageControl(
      {required this.redValue,
      required this.blueValue,
      required this.greenValue});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            children: [
              SizedBox(
                height: 20.5,
              ),
              SizedBox(
                height: 20.0,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    width: 286.0,
                    height: 156.0,
                    padding: EdgeInsets.fromLTRB(20.0, 20.0, 20.0, 32.0),
                    decoration: BoxDecoration(
                      color: Color(0xFFBDBFF8),
                      borderRadius: BorderRadius.only(
                        topRight: Radius.circular(24),
                        bottomLeft: Radius.circular(24),
                      ),
                      border: Border.all(
                        width: 1.0,
                        color: Color(0xFF000000),
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Color(0x8061007A),
                          offset: Offset(0, 0),
                          blurRadius: 8.5600004196167,
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Column(
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      '10/${redValue}',
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
                                SizedBox(
                                  height: 10.0,
                                ),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      'blue\nboxes',
                                      style: TextStyle(
                                        color: Colors.black,
                                        fontSize: 19.0,
                                        fontFamily: 'regular',
                                        fontWeight: FontWeight.bold,
                                      ),
                                      textAlign: TextAlign.center,
                                    ),
                                  ],
                                )
                              ],
                            )
                          ],
                        )
                      ],
                    ),
                  ),
                ],
              ),
              SizedBox(
                height: 10.0,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    width: 286.0,
                    height: 156.0,
                    padding: EdgeInsets.fromLTRB(20.0, 20.0, 20.0, 32.0),
                    decoration: BoxDecoration(
                      color: Color(0xFFFFA0A0),
                      borderRadius: BorderRadius.only(
                        topRight: Radius.circular(24),
                        bottomLeft: Radius.circular(24),
                      ),
                      border: Border.all(
                        width: 1.0,
                        color: Color(0xFF000000),
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Color(0x8061007A),
                          offset: Offset(0, 0),
                          blurRadius: 8.5600004196167,
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Column(
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      '10/${blueValue}',
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
                                SizedBox(
                                  height: 10.0,
                                ),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      'red\nboxes',
                                      style: TextStyle(
                                        color: Colors.black,
                                        fontSize: 19.0,
                                        fontFamily: 'regular',
                                        fontWeight: FontWeight.bold,
                                      ),
                                      textAlign: TextAlign.center,
                                    ),
                                  ],
                                )
                              ],
                            )
                          ],
                        )
                      ],
                    ),
                  ),
                ],
              ),
              SizedBox(
                height: 10.0,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    width: 286.0,
                    height: 156.0,
                    padding: EdgeInsets.fromLTRB(20.0, 20.0, 20.0, 32.0),
                    decoration: BoxDecoration(
                      color: Color(0xFFBDF8CE),
                      borderRadius: BorderRadius.only(
                        topRight: Radius.circular(24),
                        bottomLeft: Radius.circular(24),
                      ),
                      border: Border.all(
                        width: 1.0,
                        color: Color(0xFF000000),
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Color(0x8061007A),
                          offset: Offset(0, 0),
                          blurRadius: 8.5600004196167,
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Column(
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      '10/${greenValue}',
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
                                SizedBox(
                                  height: 10.0,
                                ),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      'green\nboxes',
                                      style: TextStyle(
                                        color: Colors.black,
                                        fontSize: 19.0,
                                        fontFamily: 'regular',
                                        fontWeight: FontWeight.bold,
                                      ),
                                      textAlign: TextAlign.center,
                                    ),
                                  ],
                                )
                              ],
                            )
                          ],
                        )
                      ],
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
