from flask import request, session
from flask_socketio import emit, join_room, leave_room, ConnectionRefusedError

from app.apis.chat.service import ChatService
from app.apis.message.service import MessageService
from app.ext.socketio import socketio
from app.ext.auth import auth_service
from app.errors.client.base import UnauthorizedException

@socketio.on('connect')
def connect():
    token = request.args.get('token')
    if not token:
        return False

    try:
        data = auth_service.authenticate(token)
    except UnauthorizedException:
        return False

    session['current_user_id'] = data.get('user_id')

@socketio.on('join')
def on_join(data):
    room = data.get('room')
    user_id = session['current_user_id']

    if room is not None:
        try:
            ChatService.get(user_id, room)
        except Exception:
            return False
        
        session['room'] = room
        join_room(room)
        emit('status', { 'message': 'joined' }, room=room)

@socketio.on('message')
def on_message(data):
    room = session['room']
    sender_user_id = session['current_user_id']
    
    message = data.get('message')
    MessageService.create(
        room,
        {
            'content': message,
            'sender_user_id': sender_user_id
        }
    )

    event = {
        'message': message,
        'sender_user_id': sender_user_id
    }
    emit('message_received', event, room=room)


# @socketio.on('left', namespace='/chat')
# def left(message):
#     """Sent by clients when they leave a room.
#     A status message is broadcast to all people in the room."""
#     room = session.get('room')
#     leave_room(room)
#     emit('status', {'message': session.get('user_name') + ' has left the room.'}, room=room)