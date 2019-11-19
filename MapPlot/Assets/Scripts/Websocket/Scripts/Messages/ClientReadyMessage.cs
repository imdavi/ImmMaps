using System;
using Newtonsoft.Json;

[JsonObject]
class ClientReadyMessage : Message
{
    private ClientReadyMessage() : base(MessageType) { }

    public static string MessageType { get; } = "client_ready";
    public static Message Message { get; } = new ClientReadyMessage();
}