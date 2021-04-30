#
import cv2
from apps.cve.cve_app import CveApp

def main(args={}):
    print('多传感器环境感知 v0.0.1')
    app = CveApp()
    app.startup(args)

if '__main__' == __name__:
    args = {}
    main(args)