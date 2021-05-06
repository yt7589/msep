#include "opencv.hpp"

using namespace std;
using namespace cv; //opencv 的命名空间

const int DETECTION_WIDTH = 320;

CascadeClassifier generateFaceDetector();
int setupVideoCapture(cv::VideoCapture& vidCap);
Mat convertToGrayScale(Mat colorFrame);
Mat resizeFrame(Mat orgFrame);
Mat equalizeFrame(Mat orgFrame);
std::vector<Rect> detectFaces(CascadeClassifier faceDetector, Mat frame);
void restoreFaceResults(Mat frame, std::vector<Rect>& faces);
void drawFacesOnFrame(Mat frame, std::vector<Rect> faces);

int main()
{
	printf("OpenCV路面感知平台 v0.0.2");
	CascadeClassifier faceDetector = generateFaceDetector();
	cout << "获取人脸检测器成功" << endl;
	cv::VideoCapture vidCap;
	if (setupVideoCapture(vidCap) != 0) {
		cerr << "获取摄像头视频失败！" << endl;
		exit(2);
	}
	cout << "获取网络摄像头视频成功" << endl;
	int num = 0;
	std::vector<Rect> faces;
	while (true) {
		cv::Mat frame;
		vidCap >> frame;
		if (frame.empty()) {
			cerr << "获取视频帧失败！" << endl;
			exit(3);
		}
		cv::Mat grayFrame = convertToGrayScale(frame);
		cv::Mat scaledFrame = resizeFrame(grayFrame);
		cv::Mat equalizedFrame = equalizeFrame(scaledFrame);
		if (num++ % 5) {
			faces = detectFaces(faceDetector, equalizedFrame);
			restoreFaceResults(frame, faces);
			cout << "检测到人脸数量：" << faces.size() << endl;
		}
		drawFacesOnFrame(frame, faces);
		imshow("实时视频", frame);
		char keyPressed = cv::waitKey(20);
		if (27 == keyPressed) {
			break;
		}
	}
	cout << "程序运行结束！" << endl;
	return 0;
}

CascadeClassifier generateFaceDetector() {
	const char* faceXmlFn = "D:\\zjkj\\opencv\\msepc\\x64\\Debug\\haarcascade_frontalface_alt2.xml";
	CascadeClassifier faceDetector;
	try {
		faceDetector.load(faceXmlFn);
	}
	catch (cv::Exception ex) {
		cout << "exception:" << endl;
	}
	if (faceDetector.empty()) {
		cerr << "载入" << faceXmlFn << "失败！" << endl;
		exit(1);
	}
	return faceDetector;
}

int setupVideoCapture(cv::VideoCapture& vidCap) {
	//if (!vidCap.open("rtsp://admin:zjkj2020@192.168.2.241:554/cam/realmonitor?channel=1&subtype=0")) {
	if (!vidCap.open(0)) {
		return 1;
	}
	return 0;
}

Mat convertToGrayScale(Mat orgFrame) {
	Mat grayFrame;
	if (orgFrame.channels() == 3) {
		cvtColor(orgFrame, grayFrame, cv::COLOR_BGR2GRAY);
	}
	else if (orgFrame.channels() == 4) {
		cvtColor(orgFrame, grayFrame, cv::COLOR_BGRA2GRAY);
	}
	else {
		grayFrame = orgFrame;
	}
	return grayFrame;
}

Mat resizeFrame(Mat orgFrame) {
	Mat dstFrame;
	float scale = orgFrame.cols / (float)DETECTION_WIDTH;
	if (orgFrame.cols > DETECTION_WIDTH) {
		int scaledHeight = cvRound(orgFrame.rows / scale);
		resize(orgFrame, dstFrame, Size(DETECTION_WIDTH, scaledHeight));
	}
	else {
		dstFrame = orgFrame;
	}
	return dstFrame;
}

Mat equalizeFrame(Mat orgFrame) {
	Mat rstFrame;
	equalizeHist(orgFrame, rstFrame);
	return rstFrame;
}

std::vector<Rect> detectFaces(CascadeClassifier faceDetector, Mat frame) {
	int flags = CASCADE_SCALE_IMAGE;
	Size minFeatureSize(20, 20);
	float searchScaleFactor = 1.1f;
	int minNeighbors = 4;
	std::vector<Rect> faces;
	faceDetector.detectMultiScale(frame, faces, searchScaleFactor, minNeighbors, flags, minFeatureSize);
	return faces;
}


void restoreFaceResults(Mat frame, std::vector<Rect>& faces) {
	float scale = frame.cols / (float)DETECTION_WIDTH;
	if (frame.cols > DETECTION_WIDTH) {
		for (int i = 0; i < (int)faces.size(); i++) {
			faces[i].x = cvRound(faces[i].x * scale);
			faces[i].y = cvRound(faces[i].y * scale);
			faces[i].width = cvRound(faces[i].width * scale);
			faces[i].height = cvRound(faces[i].height * scale);
		}
	}
	for (int i = 0; i < (int)faces.size(); i++) {
		if (faces[i].x < 0) {
			faces[i].x = 0;
		}
		if (faces[i].y < 0) {
			faces[i].y = 0;
		}
		if (faces[i].x + faces[i].width > frame.cols) {
			faces[i].x = frame.cols - faces[i].width;
		}
		if (faces[i].y + faces[i].height > frame.rows) {
			faces[i].y = frame.rows - faces[i].height;
		}
	}
}

void drawFacesOnFrame(Mat frame, std::vector<Rect> faces) {
	for (int i = 0; i < (int)faces.size(); i++) {
		rectangle(frame, faces[i], Scalar(255, 0, 0), 6, 1, 0);
	}
}


























void learn() {
	Mat srcImage = imread("E:\\awork\\zjkj\\work\\stpbe\\bk\\pic_20201226153300110_蓝粤EU977A.jpg");
	Mat temImage, dstImage1;
	temImage = srcImage;
	//尺寸调整
	resize(temImage, dstImage1, Size(0, 0), 1.0, 1.0, INTER_LINEAR);     //长宽缩小1/4
	imshow("车辆识别", dstImage1);
	Mat M(2, 2, CV_8UC3, Scalar(0, 0, 255));
	cout << "M = " << endl << " " << M << endl << endl;
}