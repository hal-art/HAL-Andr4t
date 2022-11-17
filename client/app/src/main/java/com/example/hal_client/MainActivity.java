package com.example.hal_client;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    Activity activity = this;
    Context context;

    static String TAG="MainActivityClass";

    @Override
    protected  void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        overridePendingTransition(0, 0);
        context=getApplicationContext();

        finish();
    }
}
