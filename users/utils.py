def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义JWT认证成功返回数据
    """
    return {
        'id': user.id,
        'rid': user.rid,
        'username': user.username,
        'mobile': user.mobile,
        'email': user.email,
        'token': token,
    }
