using System;

// Defines all client event delegate protocols

public delegate void ClientConnectedAction();
public delegate void ClientDisconnectedAction();
public delegate void MessageReceivedAction(Message message);
public delegate void ClientErrorAction(Exception exception);
public delegate void RawMessageReceivedAction(String message);
