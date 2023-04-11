# Applied-Crypto-Project
Simple Secret Sharing Algorithm

Includes 3 scripts:

	host.py -
	Uses polynomial function f(x) to generate "shadows" for 5 random numbers.
	Allows local users to connect and sends unique pairs of x and f(x) to each client

	client.py -
	Connects to host.py and obtains one pair of x and f(x)
	Optionally sends the pair to third_party.py to compute the secret

	third_party.py -
	Receives 3 pairs of x and f(x) from clients and solves for the "secret" polynomial constants A, B and C.
	Uses matrix multiplication to solve system of equations based on client input

To-Do:
	Planning on rewritting to implement Shamir's Secret Sharing Algorithm... Not 100% on validity of current method
