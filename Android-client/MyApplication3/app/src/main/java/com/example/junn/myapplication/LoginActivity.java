package com.example.junn.myapplication;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
//import java.util.logging.Handler;
import java.util.logging.LogRecord;


public class LoginActivity extends Activity implements View.OnClickListener{

    public static final int SHOW_RESPONSE = 0;
    static int PORT_ = 8000;
    private Button login_button;
    private EditText login_user;
    private EditText login_pass;
    private TextView responseText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        login_button = (Button)findViewById(R.id.loginbutton);
        login_user = (EditText)findViewById(R.id.loginuser);
        login_pass = (EditText)findViewById(R.id.loginpass);
        responseText = (TextView)findViewById(R.id.abc);
        login_button.setOnClickListener(this);
    }

    private Handler handler = new Handler() {

        public void handleMessage(Message msg) {
            switch (msg.what){
                case SHOW_RESPONSE:
                    String response = (String) msg.obj;
                    responseText.setText(response);
            }

        }

    };

    @Override
    public void onClick(View v) {
        //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
        if (v.getId() == R.id.loginbutton){
            //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
            Lgn();
        }
    }

    private  void getStringFromText(){
            String user = login_user.getText().toString();
            String pass = login_pass.getText().toString();
            Toast.makeText(LoginActivity.this, user.concat(pass), Toast.LENGTH_SHORT).show();
    }

    private void Lgn() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
                try {
                    //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
                    HttpURLConnection connection = null;
                    URL url = new URL("http://114.215.84.22:8000");
                    connection=(HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("POST");
                    //InputStream in = connection.getInputStream();
                    DataOutputStream out = new DataOutputStream(connection.getOutputStream());
                    out.writeBytes("username=junn&password=ljn7168396");
                    InputStream in = connection.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    StringBuilder response = new StringBuilder();
                    String line;
                    while((line = reader.readLine()) != null){
                        response.append(line);
                    }
                    Message message = new Message();
                    message.what = SHOW_RESPONSE;
                    message.obj = response.toString();
                    handler.handleMessage(message);
                }
                catch (Exception e){
                    //Toast.makeText(LoginActivity.this, "You clicked aaaaaaaButton", Toast.LENGTH_SHORT).show();
                }
            }
        }).start();
    }


}
