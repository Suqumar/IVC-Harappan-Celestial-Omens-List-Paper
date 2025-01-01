import ephem
import math

def ephem_fn():
    # Observer location (optional)
    observer = ephem.Observer()
    observer.lat = '68.1357'  # Replace with the observer's latitude in degrees
    observer.lon = '27.3243'  # Replace with the observer's longitude in degrees
    # Set observer's date to a specific date in BC
    specific_date_bc = ephem.Date('-2596/11/05 12:00:00')  # Replace with the desired BC date/time
    observer.date = specific_date_bc

    # Create two celestial objects
    obj1 = ephem.FixedBody()  # Venus
    obj1._ra = ephem.hours(13 + 54/60 + 30.25/3600)  # Venus' RA in hours
    obj1._dec = ephem.degrees(-(12 + 10/60 + 25.9/3600))  # Venus' Declination in degrees

    obj2 = ephem.FixedBody()  # Mercury
    obj2._ra = ephem.hours(13 + 44/60 + 57.55/3600)  # Mercury's RA in hours
    obj2._dec = ephem.degrees(-(12 + 51/60 + 26.8/3600))  # Mercury's Declination in degrees

    # Compute positions for the objects
    # observer.date = ephem.now()  # Update observer's date/time if needed
    obj1.compute(observer)
    obj2.compute(observer)

    # Compute the angular separation between the two objects
    sep = ephem.separation(obj1, obj2)
    angle_sep = ephem.degrees(sep) #float(sep)  # Convert the separation to degrees
    print(f"Angular separation between the objects: Nov. 5 2596 BC ****** {angle_sep} degrees")

# Convert degrees, minutes, and seconds to decimal degrees
def dms_to_dd(hrs, minutes, seconds):
    return hrs + minutes / 60 + seconds / 3600

def angular_fn():

    # Convert RA and Declination values from degrees, minutes, and seconds to decimal degrees
    venus_ra = dms_to_dd(13, 54, 30.25)
    venus_dec = dms_to_dd(12, 10, 25.9) * -1
    mercury_ra = dms_to_dd(13, 44, 57.55)
    mercury_dec = dms_to_dd(12, 51, 26.8) * -1

    # Convert decimal degrees to radians for trigonometric functions
    venus_ra_rad = math.radians(venus_ra * 15)  # RA is converted to degrees and then radians
    venus_dec_rad = math.radians(venus_dec)
    mercury_ra_rad = math.radians(mercury_ra * 15)  # RA is converted to degrees and then radians
    mercury_dec_rad = math.radians(mercury_dec)

    # Calculate the angular separation using the spherical law of cosines
    angular_sep = math.acos((math.sin(venus_dec_rad) * math.sin(mercury_dec_rad)) +
                            (math.cos(venus_dec_rad) * math.cos(mercury_dec_rad) * math.cos(venus_ra_rad - mercury_ra_rad))
                            )

    # Convert the angular separation from radians to degrees
    angular_sep_deg = math.degrees(angular_sep)

    print(f"The angular separation between Venus and Mercury is approximately Nov. 5 2596 BC {angular_sep_deg:.2f} degrees.")

# print('Method 1 to find the angular separation using python ephem function: From Ephem')
# ephem_fn()

print('Method 2 to find the angular separation using the math formula :From angular')
angular_fn()