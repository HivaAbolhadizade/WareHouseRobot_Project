// ignore_for_file: use_key_in_widget_constructors, avoid_print, prefer_const_constructors_in_immutables, prefer_const_constructors, prefer_const_literals_to_create_immutables, empty_statements, must_be_immutable, unnecessary_brace_in_string_interps

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MyControlPage extends StatelessWidget {
  Future<void> sendMovementRequest(String endpoint) async {
    final url = Uri.parse('http://192.168.126.22:5000/${endpoint}');

    try {
      final response = await http.get(url);
      print(response);

      if (response.statusCode == 200) {
        print(response.body);
        print('Request successful');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error sending request: $e');
    }
  }

  void moveForward() {
    print('Move Forward');
    sendMovementRequest('move_forward');
  }

  void moveBackward() {
    print('Move Backward');
    sendMovementRequest('move_backward');
  }

  void moveLeft() {
    print('Move Left');
    sendMovementRequest('move_left');
  }

  void moveRight() {
    print('Move Right');
    sendMovementRequest('move_right');
  }

  bool cth = true;
  void stopStart() {
    if (cth == true) {
      sendMovementRequest('catch');
      print('catch');
      cth = false;
    } else {
      sendMovementRequest('drop');
      print('drop');
      cth = true;
    }

    ;
  }

  @override
  Widget build(BuildContext context) {
    return MyControlPageContent(
      moveForward: moveForward,
      moveBackward: moveBackward,
      moveLeft: moveLeft,
      moveRight: moveRight,
      stopStart: stopStart,
    );
  }
}

class MyControlPageContent extends StatelessWidget {
  final VoidCallback moveForward;
  final VoidCallback moveBackward;
  final VoidCallback moveLeft;
  final VoidCallback moveRight;
  final VoidCallback stopStart;

  MyControlPageContent({
    required this.moveForward,
    required this.moveBackward,
    required this.moveLeft,
    required this.moveRight,
    required this.stopStart,
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
                        'http://192.168.126.22:5000/stream', // Replace with your actual image URL
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(
                height: 40.0,
              ),
              Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // Forward Button
                        ElevatedButton(
                          onPressed: () => moveForward(),
                          style: ButtonStyle(
                            fixedSize: MaterialStateProperty.all<Size>(
                              Size(40.0,
                                  40.0), // Set the width and height of the button
                            ),
                            backgroundColor: MaterialStateProperty.all<Color>(
                                Color(0xFFE1E1E1)),
                            shape: MaterialStateProperty.all<
                                RoundedRectangleBorder>(
                              RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(4000.0),
                                side: BorderSide(
                                  color: Colors.black, // Set the border color
                                  width: 2.0, // Set the border width
                                ), // Set border radius
                                // You can customize other properties like border color, border width, etc.
                              ),
                            ),
                          ),
                          child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/up.png', // Replace with the actual path to your asset
                                  width: 30, // Adjust the width as needed
                                  height: 30, // Adjust the height as needed
                                ),
                                SizedBox(height: 8.0),
                              ]),
                        ),
                        // Backward Button
                      ],
                    ),
                    SizedBox(height: 20),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        ElevatedButton(
                          onPressed: () => moveLeft(),
                          style: ButtonStyle(
                            fixedSize: MaterialStateProperty.all<Size>(
                              Size(40.0,
                                  40.0), // Set the width and height of the button
                            ),
                            backgroundColor: MaterialStateProperty.all<Color>(
                                Color(0xFFE1E1E1)),
                            shape: MaterialStateProperty.all<
                                RoundedRectangleBorder>(
                              RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(4000.0),
                                side: BorderSide(
                                  color: Colors.black, // Set the border color
                                  width: 2.0, // Set the border width
                                ), // Set border radius
                                // You can customize other properties like border color, border width, etc.
                              ),
                            ),
                          ),
                          child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/left.png', // Replace with the actual path to your asset
                                  width: 30, // Adjust the width as needed
                                  height: 30, // Adjust the height as needed
                                ),
                                SizedBox(height: 8.0),
                              ]),
                        ),

                        ElevatedButton(
                            onPressed: () => stopStart(),
                            style: ButtonStyle(
                              fixedSize: MaterialStateProperty.all<Size>(
                                Size(60.0,
                                    60.0), // Set the width and height of the button
                              ),
                              backgroundColor: MaterialStateProperty.all<Color>(
                                  Colors.white),
                              shape: MaterialStateProperty.all<
                                  RoundedRectangleBorder>(
                                RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(4000.0),
                                  side: BorderSide(
                                    color: Colors.black, // Set the border color
                                    width: 2.0, // Set the border width
                                  ), // Set border radius
                                  // You can customize other properties like border color, border width, etc.
                                ),
                              ),
                            ),
                            child: Text(
                              'Catch/Drop',
                              style: TextStyle(
                                color: Colors.black,
                                fontSize: 7.0,
                                fontFamily: 'regular',
                                fontWeight: FontWeight.bold,
                              ),
                            )),
                        // Right Button
                        ElevatedButton(
                          onPressed: () => moveRight(),
                          style: ButtonStyle(
                            fixedSize: MaterialStateProperty.all<Size>(
                              Size(40.0,
                                  40.0), // Set the width and height of the button
                            ),
                            backgroundColor: MaterialStateProperty.all<Color>(
                                Color(0xFFE1E1E1)),
                            shape: MaterialStateProperty.all<
                                RoundedRectangleBorder>(
                              RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(4000.0),
                                side: BorderSide(
                                  color: Colors.black, // Set the border color
                                  width: 2.0, // Set the border width
                                ), // Set border radius
                                // You can customize other properties like border color, border width, etc.
                              ),
                            ),
                          ),
                          child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/right.png', // Replace with the actual path to your asset
                                  width: 30, // Adjust the width as needed
                                  height: 30, // Adjust the height as needed
                                ),
                                SizedBox(height: 8.0),
                              ]),
                        ),
                      ],
                    ),
                    SizedBox(height: 20),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // Bottom Button
                        ElevatedButton(
                          onPressed: () => moveBackward(),
                          style: ButtonStyle(
                            fixedSize: MaterialStateProperty.all<Size>(
                              Size(40.0,
                                  40.0), // Set the width and height of the button
                            ),
                            backgroundColor: MaterialStateProperty.all<Color>(
                                Color(0xFFE1E1E1)),
                            shape: MaterialStateProperty.all<
                                RoundedRectangleBorder>(
                              RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(4000.0),
                                side: BorderSide(
                                  color: Colors.black, // Set the border color
                                  width: 2.0, // Set the border width
                                ), // Set border radius
                                // You can customize other properties like border color, border width, etc.
                              ),
                            ),
                          ),
                          child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/down.png', // Replace with the actual path to your asset
                                  width: 30, // Adjust the width as needed
                                  height: 30, // Adjust the height as needed
                                ),
                                SizedBox(height: 8.0),
                              ]),
                        ),
                      ],
                    ),
                    SizedBox(height: 20),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    ));
  }
}
