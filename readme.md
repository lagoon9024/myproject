## Raspberry PI 활용 Face Detecting additional project ##

### FUNCTIONAL SPECIFICATION ###
- 프로그램 실행 후 카메라의 위치를 조정, 원하는 각도에서 얼굴 인식이 되는지 확인
- 종료 시간 설정
- 해당 각도 얼굴 인식이 수 초간 연속 확인되면 자동으로 서비스 시작
- 종료 시간에 프로그램 자동 종료 및 데이터 반환
---
### TECHNICAL SPECIFICATION ###
1. raspberry pi zero의 camera module로 사람의 얼굴 실시간 촬영
2. 촬영 된 영상기반 face detecting을 수행, detecting 연속 시간을 반환
- python
- OpenCV face detecting library
3. 서비스 종료 시 반환 된 시간을 기반으로 DB저장
- MySQL or MongoDB
4. DB를 기반으로 한 개인 웹서비스 제공
- RESTful API
- Nodejs or Django
