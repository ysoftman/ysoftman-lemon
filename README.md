# github 을 pip 패키지로 설치하기

## build this test

```bash
# local 실행
python -m lemon 1 20 300 -1 99

# pip => pip3(python3)
# local 에서 배포(설치)
pip install .

# github에서 기준으로 설치
pip install git+https://github.com/ysoftman/ysoftman-lemon

# 설치 확인
pip list | grep ysoftman_lemon

# 패키지 사용하기
python lemon_package_test.py

# 패키지를 설치하면 ysoftman-lemon 명령 실행 예시
ysoftman-lemon
ysoftman-lemon 123
ysoftman-lemon 1 20 300 -1 99
```
