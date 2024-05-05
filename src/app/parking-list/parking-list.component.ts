import { Component, OnInit } from '@angular/core';
import { ParkingService } from '../parking.service';

@Component({
  selector: 'app-parking-list',
  standalone: true,
  imports: [],
  providers: [ParkingService],
  templateUrl: './parking-list.component.html',
  styleUrl: './parking-list.component.css'
})
export class ParkingListComponent implements OnInit{
  parkings_list: any;


  constructor( private parkingService: ParkingService ) {}


  ngOnInit(): void {
      this.parkingService.getParkings().subscribe((data) =>{
        this.parkings_list = data;
        
        for(let a of this.parkings_list.result.items){
          console.log(a);
        }
      })
  }

}
