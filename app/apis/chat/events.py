from flask_socketio import emit, join_room, leave_room

from app.apis.message.service import MessageService
from app.ext.socketio import socketio

@socketio.on('join')
def on_join(data):
    token = data.get('token')
    room = data.get('room')

    if room is not None:
        #TODO verify if user has permisson to access room
        ...

        join_room(room)
        emit('status', { 'message': 'joined.' }, room=room)

@socketio.on('message')
def on_message(data):
    room = data.get('room')
    
    token = data.get('token')
    # TODO extract user_id from token
    sender_user_id = 'extract from token'

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