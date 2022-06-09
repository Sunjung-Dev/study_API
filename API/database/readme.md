# myql 8 버전 설치하기 

### rpm 설치하기 
```
sudo yum install https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
```


### yum으로 설치하기 
```
sudo yum install mysql-community-server
```

### 이렇게해도 안되는 경우 아래와 같은 에러 발생하는 경우 
```
The GPG keys listed for the "MySQL 8.0 Community Server" repository are already installed but they are not correct for this package.
Check that the correct key URLs are configured for this repository.
```
 
 > #### 해결 방법
  ```
  sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
  ```
