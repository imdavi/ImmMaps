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
        Debug.Log("Status after init: " + WebsocketManager.IsConnected);
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
        //else if(message is HeightmapMessage)
        //{
        //    Debug.Log("Heightmap received");
        //}
    }

    private void RegisterMessageTypes()
    {
        //SerializationUtils.RegisterMessageType<HeightmapMessage>(HeightmapMessage.MessageType);
        SerializationUtils.RegisterMessageType<TextMessage>(TextMessage.MessageType);
    }
}