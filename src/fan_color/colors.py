from openrgb import OpenRGBClient
from openrgb.utils import DeviceType, RGBColor


class ColorManager:

    COLDEST_COLOR = 180
    WARMEST_COLOR = 0
    SATURATION = 100
    INTENSITY = 60

    def __init__(self, address='127.0.0.1', port=6742):
        self.openrgb_client = OpenRGBClient(address=address, port=port)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.openrgb_client.disconnect()

    def _calculate_hue(self, avg_temp):
        """Returns the hue value for temperature.
        It may seem odd that I am decreasing COLDEST_COLOR but on the HSV space,
        the colder colors have higher value than warmer colors."""

        value = self.COLDEST_COLOR - avg_temp * 2
        return value if value >= self.WARMEST_COLOR else self.WARMEST_COLOR

    def set_color(self, avg_temp, device_type=DeviceType.MOTHERBOARD):
        motherboard_rgb = self.openrgb_client.get_devices_by_type(device_type)[0]  # TODO: create config with device types

        for zone in motherboard_rgb.zones:
            zone.set_color(RGBColor.fromHSV(self._calculate_hue(avg_temp), self.SATURATION, self.INTENSITY))
