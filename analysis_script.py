
import os, numpy as np, pandas as pd, matplotlib.pyplot as plt

def simulate_gbm(S0,mu,sigma,T,N,M):
    dt=T/N
    paths=np.zeros((M,N+1)); paths[:,0]=S0
    for t in range(1,N+1):
        Z=np.random.normal(size=M)
        paths[:,t]=paths[:,t-1]*np.exp((mu-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*Z)
    return paths

def monte_carlo_call(S0,K,T,r,sigma,M,N):
    dt=T/N; S=S0*np.ones(M)
    for t in range(N):
        Z=np.random.normal(size=M)
        S=S*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*Z)
    payoff=np.maximum(S-K,0)
    return np.exp(-r*T)*np.mean(payoff)

def main():
    os.makedirs("project5_finance",exist_ok=True)
    base_dir="project5_finance"
    S0,mu,sigma,T,N,M=100,0.05,0.2,1,252,1000
    paths=simulate_gbm(S0,mu,sigma,T,N,M)
    pd.DataFrame(paths[:5].T).to_csv(os.path.join(base_dir,"gbm_samplepaths.csv"),index=False)

    import matplotlib.pyplot as plt
    plt.figure()
    for i in range(10): plt.plot(paths[i],alpha=0.7)
    plt.xlabel("Time step"); plt.ylabel("Stock Price")
    plt.title("GBM: 10 Simulated Stock Price Paths")
    plt.tight_layout(); plt.savefig(os.path.join(base_dir,"fig_gbm_paths.png"),dpi=200); plt.close()

    plt.figure(); plt.hist(paths[:,-1],bins=30,density=True,alpha=0.7)
    plt.xlabel("Final Stock Price at T=1"); plt.ylabel("Density")
    plt.title("GBM Final Price Distribution")
    plt.tight_layout(); plt.savefig(os.path.join(base_dir,"fig_gbm_final_distribution.png"),dpi=200); plt.close()

    K=100; r=0.05
    trial_sizes=[100,1000,5000,10000,20000]; results=[]
    for M in trial_sizes:
        price=monte_carlo_call(S0,K,T,r,sigma,M,N)
        results.append({"M":M,"estimated_price":price})
    df=pd.DataFrame(results); df.to_csv(os.path.join(base_dir,"option_pricing_convergence.csv"),index=False)

    plt.figure(); plt.plot(df["M"],df["estimated_price"],marker="o")
    plt.axhline(y=df["estimated_price"].iloc[-1],color="red",linestyle="--",label="Approx. limit")
    plt.xscale("log"); plt.xlabel("Number of simulations (log)")
    plt.ylabel("Estimated Call Price"); plt.title("Monte Carlo Option Pricing Convergence")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(base_dir,"fig_option_convergence.png"),dpi=200); plt.close()

if __name__=="__main__": main()
