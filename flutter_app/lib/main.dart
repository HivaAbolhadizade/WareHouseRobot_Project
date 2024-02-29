// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, prefer_const_literals_to_create_immutables, sized_box_for_whitespace, must_be_immutable, library_private_types_in_public_api, avoid_print, unnecessary_brace_in_string_interps

import 'package:flutter/material.dart';
import 'package:flutter_application_2/sensors_page.dart';
import 'auto_page.dart';
import 'entity_page.dart';
import 'manual_page.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String redValue = ''; // Declare the variables here
  String greenValue = '';
  String blueValue = '';
  Future<void> sendRequest(String endpoint) async {
    final url = Uri.parse('http://192.168.126.22:5000/${endpoint}');

    try {
      final response = await http.get(url);

      if (response.statusCode == 200) {
        print('Request successful');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error sending request: $e');
    }
  }

  void onTabTapped(int index) {
    // Your onPressed functionality goes here
    setState(() {
      _currentIndex = index;
      // Call the appropriate request function based on the selected index
      switch (index) {
        case 0:
          sendHomeRequest();
          break;
        case 1:
          sendManualRequest();
          break;
        case 2:
          sendAutoRequest();
          break;
        case 3:
          sendEntityRequest();
          break;
        case 4:
          sendSensorsRequest();
          break;
        // Add more cases if you have additional tabs
      }
    });
  }

  void sendHomeRequest() {
    // Logic to send a request related to the "Home" tab
    sendRequest('Home');
    // Add your actual request logic here
  }

  void sendManualRequest() {
    // Logic to send a request related to the "Manual" tab
    sendRequest('Manual');
    // Add your actual request logic here
  }

  void sendAutoRequest() {
    // Logic to send a request related to the "Auto" tab
    sendRequest('Auto');
    // Add your actual request logic here
  }

  void sendEntityRequest() {
    // Logic to send a request related to the "Entity" tab
    sendRequest('Entity');
    // Add your actual request logic here
  }

  void sendSensorsRequest() {
    // Logic to send a request related to the "Sensors" tab
    print('Sensor');
    // Add your actual request logic here
  }

  Color greenButtonColor = Color(0xFFA7ECB2);
  Color whiteButtonColor = Colors.white;
  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
          onTabTapped(index);
        },
        items: [
          BottomNavigationBarItem(
            icon: Image.asset("assets/home.png"),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Image.asset("assets/manual.png"),
            label: 'Manual',
          ),
          BottomNavigationBarItem(
            icon: Image.asset("assets/auto.png"),
            label: 'Auto',
          ),
          BottomNavigationBarItem(
            icon: Image.asset("assets/store.png"),
            label: 'entitiy',
          ),
          BottomNavigationBarItem(
            icon: Image.asset("assets/sensors.png"),
            label: 'Sensors',
          ),
        ],
      ),
      body: IndexedStack(
        index: _currentIndex,
        children: [
          HomeContent(),
          MyControlPage(),
          MyAutoPage(),
          MyEntityPage(
            redValue: redValue,
            blueValue: blueValue,
            greenValue: greenValue,
          ),
          MySensorPage(),
          // Add other pages here if needed
        ],
      ),
    ));
  }
}

class HomeContent extends StatelessWidget {
  String redValue = '';
  String greenValue = '';
  String blueValue = '';
  final TextEditingController _redController = TextEditingController();
  final TextEditingController _greenController = TextEditingController();
  final TextEditingController _blueController = TextEditingController();

  void updateColorValues() {
    // Method to update color values
    redValue = _redController.text;
    greenValue = _greenController.text;
    blueValue = _blueController.text;
  }

  // Text editing controllers for the input fields

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: PreferredSize(
          preferredSize:
              Size.fromHeight(70.0), // Set your preferred height here
          child: AppBar(
            backgroundColor: Colors.white,
            elevation: 0, // Remove the shadow
            title: Padding(
              padding: const EdgeInsets.only(top: 15.0),
              child: Center(
                child: Text(
                  'Welcome',
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 30.0,
                    fontFamily: 'YourFontFamily',
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ),
          ),
        ),
        body: SingleChildScrollView(
          child: Container(
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
                    height: 30.0,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      InputBox(
                        label: 'Rasberry IP',
                        color: Color(0xFFF0F8F8),
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
                        width: 291.0,
                        height: 148.0,
                        decoration: BoxDecoration(
                          color: Color(0xFFA7ECEC),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(
                            color: Colors.black,
                            width: 1.0,
                          ),
                        ),
                        child: Center(
                          child: Text(
                            'Hello\nHow many boxes do\nyou have?',
                            style: TextStyle(
                              color: Colors.black,
                              fontSize: 20.0,
                              fontFamily: 'regular',
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(height: 25.0),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      LabeledInputBox(
                        label: 'Red',
                        color: Color(0xFFECA7A7),
                        onTextChanged: (value) {
                          // Use a text editing controller to get the value
                          _redController.text = value;
                        },
                      ),
                      LabeledInputBox(
                        label: 'Blue',
                        color: Color(0xFF88CBCB),
                        onTextChanged: (value) {
                          // Use a text editing controller to get the value
                          _blueController.text = value;
                        },
                      ),
                      LabeledInputBox(
                        label: 'Green',
                        color: Color(0xFFA7ECB2),
                        onTextChanged: (value) {
                          // Use a text editing controller to get the value
                          _greenController.text = value;
                        },
                      ),
                    ],
                  ),
                  SizedBox(
                    height: 20.0,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          // Call the updateColorValues method to update the variables
                          updateColorValues();
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => MyEntityPage(
                                    redValue: redValue,
                                    blueValue: blueValue,
                                    greenValue: greenValue)),
                          );
                          print('Red: $redValue');
                          print('Blue: $blueValue');
                          print('Green: $greenValue');
                          // Add any other logic you want to perform on button press
                          //d your button click logic here
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor:
                              Color(0xFF62AC28), // Background color
                          padding: EdgeInsets.symmetric(
                              horizontal: 20, vertical: 10),

                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8.0),
                              side:
                                  BorderSide(color: Colors.black, width: 1.5)),

                          fixedSize: Size(143, 37),
                        ),
                        child: Text(
                          'save',
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
                    height: 10.0,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          // Add your button click logic here
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white, // Background color
                          padding: EdgeInsets.symmetric(
                              horizontal: 20, vertical: 10),

                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8.0),
                              side:
                                  BorderSide(color: Colors.black, width: 1.5)),

                          fixedSize: Size(143, 37),
                        ),
                        child: Text(
                          'Reset',
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
                ],
              ),
            ),
          ),
        ));
  }
}

class LabeledInputBox extends StatelessWidget {
  final String label;
  final Color color;
  final Function(String) onTextChanged;

  const LabeledInputBox(
      {required this.label, required this.color, required this.onTextChanged});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          label,
          style: TextStyle(
            color: Colors.black,
            fontSize: 20.0,
            fontFamily: 'regular',
            fontWeight: FontWeight.bold,
          ),
        ),
        Container(
          width: 80.0,
          height: 40.0, // Adjust the width as needed
          child: TextField(
            style: TextStyle(
              color: Colors.black,
              fontSize: 20.0,
              fontFamily: 'regular',
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
            onChanged: (text) {
              // Call the onTextChanged callback when the text changes
              onTextChanged(text);
            },
            decoration: InputDecoration(
              filled: true,
              fillColor: color,
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(30.0),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class InputBox extends StatelessWidget {
  final String label;
  final Color color;

  const InputBox({required this.label, required this.color});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          label,
          style: TextStyle(
            color: Colors.black,
            fontSize: 20.0,
            fontFamily: 'regular',
            fontWeight: FontWeight.bold,
          ),
        ),
        Container(
          width: 278.0,
          height: 40.0, // Adjust the width as needed
          child: TextField(
            style: TextStyle(
              color: Colors.black,
              fontSize: 20.0,
              fontFamily: 'regular',
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
            decoration: InputDecoration(
              filled: true,
              fillColor: color,
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10.0),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
