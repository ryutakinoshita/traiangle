

# class Review(models.Model):
#     """レビューモデル"""
#     target=models.ForeignKey(Listing,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default='退会済みのユーザー')
#     answer_text=models.TextField(max_length=300,blank=True,null=True)
#     time=models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.answer_text