from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'game/index.html')

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6],  # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return board[condition[0]]
    return None

def make_move(request):
    board = request.GET.get('board').split(',')
    player = request.GET.get('player')
    position = int(request.GET.get('position'))

    if board[position] == '':
        board[position] = player
    
    winner = check_winner(board)
    
    return JsonResponse({
        'board': board,
        'winner': winner
    })
