from functools import wraps
from flask import session, redirect, flash
from app.models.user import User

def login_required():
  def inner(function):
      @wraps (function)
      def wrap(*args, **kwargs):
         
         if 'user_id' not in session:
            flash("You're not logged in!!", 'info')
            return redirect('/')
         
         user = User.get_by_id(session['user_id'])


         return function(user, *args, **kwargs) #allows you to pass variables through without having to name them
    

      return wrap
  
  return inner