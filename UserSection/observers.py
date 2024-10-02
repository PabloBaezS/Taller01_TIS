def notify_admin_new_comment(comment):
    # Simulación de una notificación a los administradores
    print(f'Nuevo comentario por {comment.user.username}: "{comment.content}"')
