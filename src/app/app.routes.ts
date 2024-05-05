import { Routes } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { MapComponent } from './map/map.component';
import { ParkingListComponent } from './parking-list/parking-list.component';

export const routes: Routes = [
    { path:'home', component: HeaderComponent },
    { path: '', redirectTo:'/home', pathMatch: 'full' },
    { path: 'map', component: MapComponent },
    { path: 'parking', component: ParkingListComponent },

];
