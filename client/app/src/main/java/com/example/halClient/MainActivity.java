package com.example.halClient;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.os.PowerManager;


public class MainActivity extends AppCompatActivity {

    Activity activity = this;
    Context context;
    static String TAG = "MainActivityClass";
    private PowerManager.WakeLock mWakeLock = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        overridePendingTransition(0, 0);
        context=getApplicationContext();
        finish();
    }
}
