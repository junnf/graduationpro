package com.example.junn.myapplication;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
//import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import com.google.gson.Gson;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import com.example.junn.myapplication.RegisterJson;
import com.google.gson.reflect.TypeToken;

public class RegisterActivity extends Activity implements View.OnClickListener {
    private Button button;
    private EditText user;
    private EditText passwd;
    private EditText passwdag;
    private EditText course;
    private EditText sex;
    public static final int GET_INFO = 0;
    //final private StringBuilder postdata;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        button = (Button)findViewById(R.id.register);
        user = (EditText)findViewById(R.id.user);
        passwd = (EditText)findViewById(R.id.pass);
        passwdag = (EditText)findViewById(R.id.passagain);
        course = (EditText)findViewById(R.id.course);
        sex = (EditText)findViewById(R.id.sex);
        button.setOnClickListener(this);
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

    private String parseJSON(String jsondata){
        StringBuilder fin_json = new StringBuilder();

        Gson gson = new Gson();
        RegisterJson json = gson.fromJson(jsondata, RegisterJson.class);
        fin_json.append(json.getName());
        fin_json.append(json.getId());
        //List<RegisterJson> RegisterList = gson.fromJson(jsondata, new TypeToken<List<RegisterJson>>() {}.getType());
        //for (RegisterJson aaa:RegisterList) {
        //     fin_json.append(aaa.getId());
        //     Toast.makeText(this,aaa.getId(),Toast.LENGTH_SHORT).show();
        //     fin_json.append(aaa.getName());
        //     Toast.makeText(this,aaa.getName(),Toast.LENGTH_SHORT).show();
        //}
        return fin_json.toString();
    }

    final private String getpost(){
        String user_s = user.getText().toString();
        String pass_s = passwd.getText().toString();
        if (pass_s.equals(passwdag.getText().toString())){
            if (!isChineseChar(user_s) && !isChineseChar(pass_s)) {
                String data = "user=" + user_s + "&password=" + pass_s + "&course=" +
                        course.getText().toString() + "&sex=" + sex.getText().toString();
                //Toast.makeText(this,data,Toast.LENGTH_SHORT).show();
                return data;
            }
        }
        else {
            Toast.makeText(this,"两次密码不同",Toast.LENGTH_SHORT).show();
            return null;
        }
        return null;
    }

    @Override
    public void onClick(View v){
        if (v.getId() == R.id.register){
            register(getpost());
        }
    }

    public Handler handler =  new Handler(){
        public void handleMessage(Message msg){
            switch (msg.what){
                case GET_INFO:
                    String json_data = (String)msg.obj;
                    //Toast.makeText(, stra, Toast.LENGTH_SHORT).show();
                    //parseJSON(json_data);
                    //user.setText(parseJSON(json_data));
                    //user.setText(json_data+"aa");

                    //Activity context
                    Toast.makeText(RegisterActivity.this, json_data, Toast.LENGTH_SHORT).show();
            }
        }
    };

    private void register(final String postd){
        new Thread(new Runnable() {
            @Override
            public void run() {
                HttpURLConnection connection = null;
                try{
                    //System.out.print(true);
                    //HttpURLConnection connection = null;
                    URL url = new URL("http://114.215.84.22:8000/register");
                    connection=(HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("POST");
                    DataOutputStream out = new DataOutputStream(connection.getOutputStream());
                    out.writeBytes(postd);
                    InputStream in = connection.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                    StringBuilder response = new StringBuilder();
                    String line;
                    while((line = reader.readLine()) != null){
                        response.append(line);
                    }
                    //parseJSON(response.toString());
                    Message message = new Message();
                    message.what = GET_INFO;
                    message.obj = parseJSON(response.toString());
                    handler.sendMessage(message);
                } catch (Exception e){
                    e.printStackTrace();
                } finally {
                    if (connection != null){
                        connection.disconnect();
                    }
                }
            }
        }).start();
    }

}
