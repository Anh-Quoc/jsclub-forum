# Before Start

Tài Nguyên + Thông Tin 

- Link Driver: [**HERE**](https://drive.google.com/drive/folders/1xvU_jPkISWlFYvw0Te6QXEVoeYVjcJRK?usp=sharing)
- Link Wiki: [**HERE**](https://gitlab.com/js-club-ctv-bcm-gen-10-group-6/jsclub-forum/-/wikis/URL)

Text Editor: `Visual Studio Code`

Cần cài đặt sẵn: `Python`

#### _Toàn bộ các command dưới đây đều chạy bằng cmd với đường dẫn project vậy nên để tiện cho việc sử dụng với `Visual Studio Code`, nên sử dụng `Command Prompt` thay cho mặc định `Terminal`_

# Step 1: Clone Project

`git clone https://gitlab.com/js-club-ctv-bcm-gen-10-group-6/jsclub-forum.git`

`cd jsclub-forum`

# Step 2: Install Package

- Install Virtual Environment vào máy tính: `pip install virtualenv`
- Tạo Virtual Environment cho project: `virtualenv env`

> Trong folder env sẽ chứa những package được dùng trong project

> Tên package và số phiên bản được chứa trong file `requirements.txt`

- Activate Virtual Environment : `.\env\Scripts\activate`

> Nếu activate thành công sẽ có `(env)` ở đầu đường dẫn. Ngoài ra `Command Prompt` trong `Visual Studio Code` sẽ tự động activate mỗi khi được bật

![Capture](https://lh3.googleusercontent.com/vzeAKl7jyzqQSti796tRu0DCwJrUzzTuTwR5jyAGkfF8uz3s_TeLZvt6FQYpfxwPuaYuqNgfIxByZJmwuLT99EdSTbIwdBFkB9uD5yYHAeWKGniZtFDt-kgn1RsTCcoUACQbrkqO65M=w2400)

> Hành động này giúp chuyển việc sử dụng sang những package nằm trong folder `env` thay vì những phiên bản đã được cài "toàn cục" ở máy tính
- Xem những package đang được cài trong folder `env`:   `pip freeze`
- Cài đặt những package cần thiết (còn thiếu) được liệt kê trong file `requirements.txt` để chạy project:   `pip install -r requirements.txt`
> Nếu cần cài thêm những package khác, chạy `pip freeze > requirements.txt` sau khi cài đặt thành công để cập nhật vào file `requirements.txt`

# Step 3: Make Your Own Branch And ... Have Fun!
