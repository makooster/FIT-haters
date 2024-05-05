import { Component, OnInit } from '@angular/core';

import {GoogleMapsModule} from '@angular/google-maps'
import { BrowserModule } from '@angular/platform-browser';



@Component({
  selector: 'app-map',
  standalone: true,
  imports: 
  [
   GoogleMapsModule,
  ],
  templateUrl: './map.component.html',
  styleUrl: './map.component.css'
})
export class MapComponent implements OnInit{


  ngOnInit(): void {
      
  }

  display: any;
    center: google.maps.LatLngLiteral = {
        lat: 22.2736308,
        lng: 70.7512555
    };
    zoom = 6;
  
    /*------------------------------------------
    --------------------------------------------
    moveMap()
    --------------------------------------------
    --------------------------------------------*/
    moveMap(event: google.maps.MapMouseEvent) {
        if (event.latLng != null) this.center = (event.latLng.toJSON());
    }
  
    /*------------------------------------------
    --------------------------------------------
    move()
    --------------------------------------------
    --------------------------------------------*/
    move(event: google.maps.MapMouseEvent) {
        if (event.latLng != null) this.display = event.latLng.toJSON();
    }

  
}
