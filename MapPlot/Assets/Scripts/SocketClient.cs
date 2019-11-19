using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SocketClient : MonoBehaviour
{

    public ImmVisWebsocketManager WebsocketManager;

    void Awake()
    {
        RegisterMessageTypes();
        InitializeWebsocketClient();
    }

    private void InitializeWebsocketClient()
    {
        if (WebsocketManager != null && !WebsocketManager.IsConnected)
        {
            WebsocketManager.Connected += ClientConnected;
            WebsocketManager.MessageReceived += MessageReceived;
            WebsocketManager.InitializeClient();
        }
    }

    private void ClientConnected()
    {
        Debug.Log("LOG - Now you can send messages!");
        WebsocketManager.Send(ClientReadyMessage.Message);
    }

    private void MessageReceived(Message message)
    {
        Debug.Log("LOG - Message received!");

        if(message is TextMessage)
        {
            Debug.Log((message as TextMessage).Text);
        }   
    }

    /*private void DisplayHeightmap(HeightmapMessage heightmapMessage)
    {
        Debug.Log("Not implemented yet!");
    }
    private void DisplayImage(ImageMessage imageMessage)
    {
        Debug.Log("Render image!");
        var spriteRenderer = gameObject.GetComponent<SpriteRenderer>();
        var texture = new Texture2D(2, 2);
        texture.LoadImage(imageMessage.Bytes);

        Sprite sprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f));
        spriteRenderer.sprite = sprite;
    }*/

    private void RegisterMessageTypes()
    {
        //SerializationUtils.RegisterMessageType<HeightmapMessage>(HeightmapMessage.MessageType);
        //SerializationUtils.RegisterMessageType<ImageMessage>(ImageMessage.MessageType);
        SerializationUtils.RegisterMessageType<TextMessage>(TextMessage.MessageType);
    }
}