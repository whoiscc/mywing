#

import sys
import os

from django.db import models
from django.utils import timezone
from angel.models import Angel


class Board(models.Model):
    updatedAt = models.DateTimeField(null=True,blank=True,editable=False)
    value = 0#uncertain

    def to_dict(self):
        for score in Score.objects.filter(board=self):
            score.set_score()
        scores_on_board=Score.objects.filter(board=self).order_by('scores')
        angels_on_board=[score.angel for score in scores_on_board]
        return_dict=[[score.angel_to_dict() for score in scores_on_board],self.updatedAt]
        return return_dict


class Score(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    scores = models.FloatField(null=True, blank=True) 


    def set_score(self):
        board_score_dict={
            1:self.angel.distribution,#uncertain 
        }
        self.scores = board_score_dict[self.board.id]
        self.save()


    def angel_to_dict(self):
        return {
            'id':self.angel.id,
            'nickname':self.angel.nickname,
            'value':self.board.value,
        }
    
      

class News(models.Model):
    title = models.CharField(null=True,blank=True,max_length=64)
    author = models.CharField(null=True,blank=True,max_length=64)
    updatedAt = models.DateTimeField(null=True,blank=True,editable=False)
    content = models.CharField(null=True,blank=True,max_length=128)
    
    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'updatedAt':self.updatedAt,
        }
