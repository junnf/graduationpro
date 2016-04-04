package com.example.junn.myapplication;

import android.app.Activity;
import android.content.Context;
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

import com.example.junn.myapplication.LoginJson;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
//import java.util.logging.Handler;
import java.util.logging.LogRecord;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import com.google.gson.Gson;




public class LoginActivity extends Activity implements View.OnClickListener{

    public static final int SHOW_RESPONSE = 0;
    static int PORT_ = 8000;
    private Button login_button;
    //get string
    private EditText login_pass;
    private EditText login_user;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        login_button = (Button)findViewById(R.id.loginbutton);
        login_user = (EditText)findViewById(R.id.loginuser);
        login_pass = (EditText)findViewById(R.id.loginpass);
        login_button.setOnClickListener(this);
    }

    private Handler handler = new Handler() {

        public void handleMessage(Message msg) {
            switch (msg.what){
                case SHOW_RESPONSE:
                    String response = (String) msg.obj;

                    //Intent intent = new Intent(LoginActivity.this, ClassTable.class);
                    //finish();
                    //startActivity(intent);

                    //responseText.setText(response);
            }

        }

    };

    private String parseJSON(String jsondata){
        StringBuilder fin_json = new StringBuilder();

        Gson gson = new Gson();
        LoginJson json = gson.fromJson(jsondata, LoginJson.class);
        if (Integer.valueOf(json.getId()).intValue() == 0) {
            return null;
        }

        //fin_json.append(json.getInformation());
        //fin_json.append(json.getId());
        return fin_json.toString();
    }

    @Override
    public void onClick(View v) {
        //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
        if (v.getId() == R.id.loginbutton){
            //Toast.makeText(LoginActivity.this, "You clicked Button", Toast.LENGTH_SHORT).show();
                    //Lgn(getpost());
            save();
        }
    }

    public static boolean isChineseChar(String str){
        boolean temp = false;
        Pattern p= Pattern.compile("[\u4e00-\u9fa5]");
        Matcher m=p.matcher(str);
        if(m.find()){
            temp =  true;
        }
        return temp;
    }

    final private String getpost(){
        String user_s = login_user.getText().toString();
        String pass_s = login_pass.getText().toString();
        if (!isChineseChar(user_s) && !isChineseChar(pass_s)) {
            String data = "user=" + user_s + "&password=" + pass_s ;
            return data;
        }
        else {
            Toast.makeText(this,"不能使用中文",Toast.LENGTH_SHORT).show();
            return null;
        }

    }

    public void save() {
        String data = "Data and fuck";
        FileOutputStream out = null;
        BufferedWriter writer = null;
        try {
            out = openFileOutput("token", Context.MODE_PRIVATE);
            writer = new BufferedWriter(new OutputStreamWriter(out));
            writer.write(data);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (writer != null) {
                    writer.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private void Lgn(final String post_data) {
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
                    DataOutputStream out = new DataOutputStream(connection.getOutputStream());
                    out.writeBytes(post_data);
                    InputStream in = connection.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    StringBuilder response = new StringBuilder();
                    String line;
                    while((line = reader.readLine()) != null){
                        response.append(line);
                    }
                    Message message = new Message();
                    message.what = SHOW_RESPONSE;
                    String _temp = null;
                    if (parseJSON(response.toString()).equals(_temp)) {
                        //return ;
                    }
                    else {
                        message.obj = parseJSON(response.toString());
                        handler.handleMessage(message);
                    }
                }
                catch (Exception e){
                    //Toast.makeText(LoginActivity.this, "You clicked aaaaaaaButton", Toast.LENGTH_SHORT).show();
                }
            }
        }).start();
    }


}
