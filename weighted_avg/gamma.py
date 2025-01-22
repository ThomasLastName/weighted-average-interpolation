
class NormSquaredRatio:
  def __init__(self,a,b):
    assert a.numel()==b.numel() and a.shape==b.shape
    self.a = a.flatten()
    self.b = b.reshape()
    self.in_dim = a.numel()
  def compute_distances_to_anchors(self,x_test):
    ab = torch.row_stack([ self.a, self.b ])
    assert ab.shape == ( 2, self.in_dim )
    assert len(x_test.shape)==2 and x_test.shape[1]==self.in_dim
    self.distances = torch.cdist( x_test, ab )
  def __call__( x_test ):
    n_test, d = x_test.shape
    assert d == self.in_dim
    try:
      dists = self.distances
    except:
      dists = self.compute_distances_to_anchors(x_test)  
    assert dists.shape == ( n_test, self.in_dim )
    all_idx = torch.arange(n_test)
    closer_one = dists.argmin(dim=1)
    x_minus_alpha_norm = dists[ all_idx, closer_one ]
    x_minus_beta_norm = dists[ all_idx, ~closer_one ]
    return 
