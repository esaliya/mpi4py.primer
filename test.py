from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
count = comm.Get_size()

print("Hello from rank: %d" %(rank))
