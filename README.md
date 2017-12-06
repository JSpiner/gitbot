# gitbot

### 기본 프로세스

- git PR webhook
- build 시작 안내 PR에 comment
- git clone후 clean build
- build 결과 로그로 남기기
- build 결과 PR에 comment

### 고민해야할것
- docker image 캐싱
- .travis와 같이 빌드환경을 설정할수있는 파일 포맷
- ssh key 관리방안 