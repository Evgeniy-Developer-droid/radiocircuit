from site_app.models import Token

def generate_token(user, name="other"):
    token = Token.objects.create(user=user, name=name)
    return str(token.token)