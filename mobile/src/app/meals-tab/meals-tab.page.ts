import { Component, OnInit } from '@angular/core';
import { MealsService } from '../services/meals/meals.service';

@Component({
  selector: 'app-meals-tab',
  templateUrl: './meals-tab.page.html',
  styleUrls: ['./meals-tab.page.scss'],
})
export class MealsTabPage implements OnInit {

  meals: any;
  loaded = false;

  constructor(private mealService: MealsService) { }

  ngOnInit() {
    this.mealService.syncMeals().subscribe((res) => {
      this.meals = res;
      this.loaded = true;
    });
  }

  handleRefresh(event) {
    setTimeout(() => {
      this.mealService.syncMeals().subscribe((res) => {
        this.meals = res;
        this.loaded = true;
      });
      event.target.complete();
    }, 2000);
  }
}
