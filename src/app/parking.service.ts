import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ParkingService {

  constructor(private http: HttpClient) { }
  
  baseURL = "https://catalog.api.2gis.com/3.0/items?q=парковка&point=76.9283,43.2567&radius=100&key=bb57b460-0d7e-4a79-a950-527905827787"

  getParkings(){
    return this.http.get("https://catalog.api.2gis.com/3.0/items?q=парковки&point=76.9283,43.2567&radius=1000&key=bb57b460-0d7e-4a79-a950-527905827787");

  }
}
