import jwt
from datetime import datetime, timedelta
SECRET_KEY = "okokokokokokokoadw"
ALLGORITHM = "HS256"

# giới hạn thời gian token kèm thông tin người dùng và mã hoá nó


def create_access_tokken(data: dict, expires_minutes: int) -> str:
    data = {"sub": 1, "email": "admin@123gmail.com"}
    expires_minutes = datetime.utcnow() + timedelta(minutes=30)
    print(expires_minutes)

    data.update({"exp": expires_minutes})
    # mã hoá payload
    token = jwt.encode(data, SECRET_KEY, algorithm=ALLGORITHM)

    return token

# kiểm tra chữ ký trao token


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALLGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token đã hết hạn"}
    except jwt.InvalidAlgorithmError:
        return {"error": "Token không đúng"}


print(
    f"Token: {create_access_tokken({'sub': 1, 'email': 'admin@123gmail.com'}, 30)}")

# câu hỏi bổ sung
# Ba phần của JWT gồm Header, Payload và Signature.

# Payload không được mã hóa mà chỉ mã hóa Base64URL nên ai cũng có thể đọc được.

# Signature dùng để xác thực tính nguyên vẹn; nếu tự sửa role trong Payload, signature sẽ không khớp và hệ thống sẽ từ chối token.
