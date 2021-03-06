import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  num_c = W.shape[1]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_train):
    scores = np.dot(X[i],W)
    
  #  print(scores.shape,X[i].shape,W.shape)
    scores_new = scores-np.max(scores)
    p = np.exp(scores_new)/np.sum(np.exp(scores_new))
    
  #  print(p.shape)
   # cor_p = p[:,y[i
    loss += -np.log(p[y[i]])  
    
    
    dscore = p
    dscore[y[i]]-=1
  #  print(dscore.shape)
    
    dW += np.dot(X[i].reshape(-1,1),dscore.reshape(1,-1))
    
  loss /= num_train
  loss += 0.5*reg*np.sum(W*W)
  dW /= num_train
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  scores = np.dot(X,W)
  scores -= np.max(scores,axis=1,keepdims=True)
  scores_exp = np.exp(scores)
  probs = scores_exp/np.sum(scores_exp,axis=1,keepdims=True)

  correct_probs = probs[np.arange(num_train),y]
  loss = np.sum(-np.log(correct_probs))/num_train
  loss += 0.5*reg*np.sum(W*W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  dscores = probs.copy()
  dscores[range(num_train),y]-=1
  dscores/=num_train

  dW = np.dot(X.T,dscores)
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

