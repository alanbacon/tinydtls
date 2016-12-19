import DTLSSocket
s = DTLSSocket.DTLSSocket(pskId=b"Client_identity", pskStore={b"Client_identity": b"secretPSK"})
s.joinMC("ff12::42", 2342, DTLSSocket.DTLS_CLIENT, b"secret")
s.sendmsg([b"Test1",], [], 0, ("ff12::42", 2342, 0, 0))
s.sendmsg([b"Test2",b"2"], [], 0, ("ff12::42", 2342, 0, 0))
del s
print("Done")
