# Device specific configs

# rpm_device is the name of the ported device
%define rpm_device ara
# rpm_vendor is used in the rpm space (the vendor doing the port)
%define rpm_vendor nokia

# Manufacturer and device name to be shown in UI
%define vendor_pretty nokia
%define device_pretty ara

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1 
%define have_led 1 

%include droid-hal-version/droid-hal-version.inc

