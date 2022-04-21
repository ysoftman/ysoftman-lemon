from setuptools import setup, find_packages

setup(
    name="ysoftman_lemon",
    version="0.0.1",
    description="test package",
    url="https://github.com/ysoftman/ysoftman-lemon",
    author="ysoftman",
    author_email="ysoftman@gmail.com",
    license="ysoftman-test",
    # packages=["lemon"], # package directory name
    packages=find_packages(),
    # ysoftman-man 명령으로 실행할 경우
    entry_points={
        'console_scripts': [
                'ysoftman-lemon=lemon.main:main',
        ]
    },
)
