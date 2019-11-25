using System;
using Newtonsoft.Json;
using UnityEngine;

[JsonObject]
public class HeightmapMessage : Message
{

    [JsonProperty] private float[][] heightmap;

    [JsonIgnore]
    public float[][] Heightmap
    {
        get { return heightmap; }
    }

    public HeightmapMessage() : base(MessageType) { }

    public static string MessageType { get; } = "heightmap";
}