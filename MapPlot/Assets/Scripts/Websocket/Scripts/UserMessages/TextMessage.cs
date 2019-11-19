using System;
using Newtonsoft.Json;
using UnityEngine;

[JsonObject]
class TextMessage : Message
{
    [JsonProperty] private string text;

    [JsonIgnore]
    public string Text
    {
        get { return text; }
    }

    public TextMessage() : base(MessageType) { }

    public static string MessageType { get; } = "text";

}