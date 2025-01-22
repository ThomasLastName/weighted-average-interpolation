
import torch
from abc import abstractmethod

class RadialGamma:
    #
    # ~~~ Store the two anchors a and b
    def __init__( self, a, b ):
        a = a if isinstance(a,torch.Tensor) else torch.tensor(a)
        b = b if isinstance(b,torch.Tensor) else torch.tensor(b)
        assert a.numel()==b.numel() and a.shape==b.shape
        self.a = a.reshape(1,-1)
        self.b = b.reshape(1,-1)
        self.in_dim = a.numel()
    #
    # ~~~ Compute the distances from an input grid to both anchors
    def compute_distances_to_anchors(self,x_test):
        ab = torch.row_stack([ self.a, self.b ])
        assert ab.shape == ( 2, self.in_dim )
        assert len(x_test.shape)==2 and x_test.shape[1]==self.in_dim
        self.distances = torch.cdist( x_test, ab )
    #
    # ~~~ 
    def fetch_distances_to_alpha_and_beta(self):
        dists = self.distances
        assert len(dists.shape)==2 and dists.shape[1]==2
        n_test = len(dists)
        all_idx = torch.arange(n_test)
        closer_one = dists.argmin(dim=1)
        x_minus_alpha_norm = dists[ all_idx, closer_one ]
        x_minus_beta_norm = dists[ all_idx, ~closer_one ]
        return closer_one, x_minus_alpha_norm, x_minus_beta_norm
    #
    # ~~~ Return the value of gamma_{a,b}(x_test)
    @abstractmethod
    def __call__( self, x_test ):
        raise NotImplementedError

class NormSquaredRatio(RadialGamma):
    def __init__(self,*args,**kwargs): super().__init__(*args,**kwargs)
    #
    def __call__( self, x_test ):
        self.compute_distances_to_anchors(x_test)
        closer_one, x_minus_alpha_norm, x_minus_beta_norm = self.fetch_distances_to_alpha_and_beta()
        return (1 - closer_one - (-1)**closer_one * (x_minus_alpha_norm/x_minus_beta_norm)**2/2).reshape(-1,1)


class NormRatio(RadialGamma):
    def __init__(self,*args,**kwargs): super().__init__(*args,**kwargs)
    #
    def __call__( self, x_test ):
        self.compute_distances_to_anchors(x_test)
        closer_one, x_minus_alpha_norm, x_minus_beta_norm = self.fetch_distances_to_alpha_and_beta()
        return (1 - closer_one - (-1)**(closer_one) * (x_minus_alpha_norm/x_minus_beta_norm)/2).reshape(-1,1)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    #
    # ~~~ Replicate first figure of the source material https://www.overleaf.com/read/zbyhqbbccrmn
    a = 1.
    b = 2.
    y_a = lambda x: torch.ones_like(x)
    y_b = lambda x: torch.ones_like(x)/2
    gamma = NormSquaredRatio(a,b)
    x_test = torch.linspace(-2,5,501).reshape(-1,1)
    plt.figure(figsize=(10,4))
    plt.plot( x_test, gamma(x_test)*y_a(x_test) + (1-gamma(x_test))*y_b(x_test), label="gamma", color="blue" )
    plt.plot( x_test, y_a(x_test), "--", label="y_a", color="grey" )
    plt.plot( x_test, y_b(x_test), "--", label="y_b", color="grey" )
    plt.tight_layout()
    plt.show()
    #
    # ~~~ Replicate second figure of the source material https://www.overleaf.com/read/zbyhqbbccrmn
    y_a = lambda x: torch.sin(x-a)
    y_b = lambda x: torch.sin(x-b)
    fig, axs = plt.subplots( 1, 2, figsize=(10,4) )
    x_test = torch.linspace(0,3,501).reshape(-1,1)
    axs[0].plot( x_test, gamma(x_test)*y_a(x_test) + (1-gamma(x_test))*y_b(x_test), label="gamma", color="blue" )
    axs[0].plot( x_test, y_a(x_test), "--", label="y_a", color="grey" )
    axs[0].plot( x_test, y_b(x_test), "--", label="y_b", color="grey" )
    axs[0].set_ylim([-0.8,0.8])
    x_test = torch.linspace(-5.5,10.5,501).reshape(-1,1)
    axs[1].plot( x_test, gamma(x_test)*y_a(x_test) + (1-gamma(x_test))*y_b(x_test), label="gamma", color="blue" )
    axs[1].plot( x_test, y_a(x_test), "--", label="y_a", color="grey" )
    axs[1].plot( x_test, y_b(x_test), "--", label="y_b", color="grey" )
    fig.tight_layout()
    plt.show()
