# Smartphone Sensor-Based Indoor Navigation

This project demonstrates a conceptual design and implementation of a sensor data collection module for an indoor navigation system using smartphone sensors. The module is developed using Python, Kivy, and Pyjnius to access and process data from various sensors on an Android smartphone.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)
- [License](#license)

## Introduction

The indoor navigation system aims to provide accurate localization and navigation within indoor environments where GPS signals are unreliable. This project focuses on the sensor data collection module, which gathers data from the accelerometer, gyroscope, magnetometer, barometer, Wi-Fi, and Bluetooth sensors of a smartphone.

## Features

- Collects and processes data from the smartphone's accelerometer, gyroscope, magnetometer, and barometer.
- Utilizes Wi-Fi and Bluetooth signals for additional localization.
- Provides a foundation for further development of data processing, fusion, and user interface modules.

## Requirements

- Python 3.x
- Kivy
- Pyjnius
- Android device with required sensors (accelerometer, gyroscope, magnetometer, barometer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/indoor-navigation.git
    cd indoor-navigation
    ```

2. Install the required Python packages:

    ```sh
    pip install kivy
    pip install pyjnius
    ```

3. Ensure you have an environment that supports Python on Android, such as Pydroid 3 or set up Buildozer to package the application.

## Usage

1. Save the script as `main.py`.

2. Run the script on your Android device using Pydroid 3 or package it using Buildozer.

    ```sh
    python main.py
    ```

3. The application will start and begin collecting sensor data. You will see the sensor readings printed in the console.

## References

- Renaudin, V., Afzal, M. H., & Lachapelle, G. (2012). "Complete triaxis accelerometer calibration and its impact on inertial navigation system performance." Sensors, 12(5), 5891-5915.
- Nilsson, J. O., Skog, I., & Handel, P. (2014). "Foot-mounted inertial navigation made easy." Proceedings of the International Conference on Indoor Positioning and Indoor Navigation (IPIN).
- Subbu, K. P., Luo, J., Wu, M. Y., & Gadh, R. (2013). "Magnetic anomaly-based localization for indoor navigation." IEEE Transactions on Instrumentation and Measurement, 62(2), 467-477.
- Zhou, C., Jiang, W., & Li, Q. (2015). "Smartphone-based indoor localization with barometer and Wi-Fi." IEEE Transactions on Consumer Electronics, 61(3), 356-365.
- Farid, Z., Nordin, R., & Ismail, M. (2013). "Recent advances in wireless indoor localization techniques and system." Journal of Computer Networks and Communications, 2013.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
