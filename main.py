from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import accelerometer, gyroscope, orientation


class SensorApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create labels to display sensor status
        self.sensor_status_labels = {
            'accelerometer': Label(text=''),
            'gyroscope': Label(text=''),
            'orientation': Label(text='')
        }

        # Add labels to layout
        for label in self.sensor_status_labels.values():
            layout.add_widget(label)

        # Check sensor availability and start data collection
        self.check_sensor_availability()

        return layout

    def check_sensor_availability(self):
        # Check accelerometer availability
        if accelerometer:
            self.sensor_status_labels['accelerometer'].text = 'Accelerometer sensor is available'
            self.collect_accelerometer_data()
        else:
            self.sensor_status_labels['accelerometer'].text = 'Accelerometer sensor is not available on this device'

        # Check gyroscope availability
        if gyroscope:
            self.sensor_status_labels['gyroscope'].text = 'Gyroscope sensor is available'
            self.collect_gyroscope_data()
        else:
            self.sensor_status_labels['gyroscope'].text = 'Gyroscope sensor is not available on this device'

        # Check orientation sensor availability
        if orientation:
            self.sensor_status_labels['orientation'].text = 'Orientation sensor is available'
            self.collect_orientation_data()
        else:
            self.sensor_status_labels['orientation'].text = 'Orientation sensor is not available on this device'

    def collect_accelerometer_data(self):
        def on_acceleration(acceleration):
            print("Accelerometer data:", acceleration)

        accelerometer.enable()
        accelerometer.bind(on_acceleration=on_acceleration)

    def collect_gyroscope_data(self):
        def on_rotation(rotation):
            print("Gyroscope data:", rotation)

        gyroscope.enable()
        gyroscope.bind(on_rotation=on_rotation)

    def collect_magnetometer_data(self):
        def on_magnetic_field(magnetic_field):
            print("Magnetometer data:", magnetic_field)

        magnetometer.enable()
        magnetometer.bind(on_magnetic_field=on_magnetic_field)

    def collect_orientation_data(self):
        def on_orientation(orientation):
            print("Orientation data:", orientation)

        orientation.enable()
        orientation.bind(on_orientation=on_orientation)


if __name__ == '__main__':
    SensorApp().run()
