import pyexiv2
import pprint
import argparse
import console

PARAM_LIST = [
    'Exif.Image.Artist',
    'Exif.Image.Copyright',
    'Exif.Image.DateTime',
    'Exif.GPSInfo.GPSVersionID',
    'Exif.Image.ExifTag',
    'Exif.Image.GPSTag',
    'Exif.Image.Make',
    'Exif.Image.Model',
    'Exif.Image.ExifTag',
]


def getParm():
    parser = argparse.ArgumentParser(
        description='Displays information embedded in the photo')
    parser.add_argument('path', type=str, help="Image Paths")
    parser.add_argument('-a', '--all', action='store_true',
                        help="All parameters")
    args = parser.parse_args()
    return [args.path, args.all]


def analysis(path):
    with pyexiv2.Image(path) as img:
        data = img.read_exif()

        info_list = list()
        for param in PARAM_LIST:
            info_list.append(data[param])
            print(param, ' : ', data[param])

    return info_list


def main():
    path = getParm()
    console.echo(path[0])
    info_list = analysis(path[0])
    console.table(info_list)
    return 0


if __name__ == "__main__":
    main()
