/**
 * gridstack.component.ts 8.2.3
 * Copyright (c) 2022 Alain Dumesny - see GridStack root license
 */
import { NgModule } from "@angular/core";
import { CommonModule } from '@angular/common';
import { GridStack } from "gridstack";
import { GridstackComponent, gsCreateNgComponents, gsSaveAdditionalNgInfo } from "./gridstack.component";
import { GridstackItemComponent } from "./gridstack-item.component";
import * as i0 from "@angular/core";
export class GridstackModule {
    constructor() {
        // set globally our method to create the right widget type
        GridStack.addRemoveCB = gsCreateNgComponents;
        GridStack.saveCB = gsSaveAdditionalNgInfo;
    }
}
GridstackModule.ɵfac = i0.ɵɵngDeclareFactory({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: GridstackModule, deps: [], target: i0.ɵɵFactoryTarget.NgModule });
GridstackModule.ɵmod = i0.ɵɵngDeclareNgModule({ minVersion: "14.0.0", version: "14.3.0", ngImport: i0, type: GridstackModule, declarations: [GridstackComponent,
        GridstackItemComponent], imports: [CommonModule], exports: [GridstackComponent,
        GridstackItemComponent] });
GridstackModule.ɵinj = i0.ɵɵngDeclareInjector({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: GridstackModule, imports: [CommonModule] });
i0.ɵɵngDeclareClassMetadata({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: GridstackModule, decorators: [{
            type: NgModule,
            args: [{
                    imports: [
                        CommonModule,
                    ],
                    declarations: [
                        GridstackComponent,
                        GridstackItemComponent,
                    ],
                    exports: [
                        GridstackComponent,
                        GridstackItemComponent,
                    ],
                }]
        }], ctorParameters: function () { return []; } });
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZ3JpZHN0YWNrLm1vZHVsZS5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbIi4uLy4uLy4uLy4uL2FuZ3VsYXIvcHJvamVjdHMvbGliL3NyYy9saWIvZ3JpZHN0YWNrLm1vZHVsZS50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7O0dBR0c7QUFFSCxPQUFPLEVBQUUsUUFBUSxFQUFFLE1BQU0sZUFBZSxDQUFDO0FBQ3pDLE9BQU8sRUFBRSxZQUFZLEVBQUUsTUFBTSxpQkFBaUIsQ0FBQztBQUUvQyxPQUFPLEVBQUUsU0FBUyxFQUFFLE1BQU0sV0FBVyxDQUFDO0FBQ3RDLE9BQU8sRUFBRSxrQkFBa0IsRUFBRSxvQkFBb0IsRUFBRSxzQkFBc0IsRUFBRSxNQUFNLHVCQUF1QixDQUFDO0FBQ3pHLE9BQU8sRUFBRSxzQkFBc0IsRUFBRSxNQUFNLDRCQUE0QixDQUFDOztBQWVwRSxNQUFNLE9BQU8sZUFBZTtJQUMxQjtRQUNFLDBEQUEwRDtRQUMxRCxTQUFTLENBQUMsV0FBVyxHQUFHLG9CQUFvQixDQUFDO1FBQzdDLFNBQVMsQ0FBQyxNQUFNLEdBQUcsc0JBQXNCLENBQUM7SUFDNUMsQ0FBQzs7NEdBTFUsZUFBZTs2R0FBZixlQUFlLGlCQVJ4QixrQkFBa0I7UUFDbEIsc0JBQXNCLGFBSnRCLFlBQVksYUFPWixrQkFBa0I7UUFDbEIsc0JBQXNCOzZHQUdiLGVBQWUsWUFYeEIsWUFBWTsyRkFXSCxlQUFlO2tCQWIzQixRQUFRO21CQUFDO29CQUNSLE9BQU8sRUFBRTt3QkFDUCxZQUFZO3FCQUNiO29CQUNELFlBQVksRUFBRTt3QkFDWixrQkFBa0I7d0JBQ2xCLHNCQUFzQjtxQkFDdkI7b0JBQ0QsT0FBTyxFQUFFO3dCQUNQLGtCQUFrQjt3QkFDbEIsc0JBQXNCO3FCQUN2QjtpQkFDRiIsInNvdXJjZXNDb250ZW50IjpbIi8qKlxyXG4gKiBncmlkc3RhY2suY29tcG9uZW50LnRzIDguMi4zXHJcbiAqIENvcHlyaWdodCAoYykgMjAyMiBBbGFpbiBEdW1lc255IC0gc2VlIEdyaWRTdGFjayByb290IGxpY2Vuc2VcclxuICovXHJcblxyXG5pbXBvcnQgeyBOZ01vZHVsZSB9IGZyb20gXCJAYW5ndWxhci9jb3JlXCI7XHJcbmltcG9ydCB7IENvbW1vbk1vZHVsZSB9IGZyb20gJ0Bhbmd1bGFyL2NvbW1vbic7XHJcblxyXG5pbXBvcnQgeyBHcmlkU3RhY2sgfSBmcm9tIFwiZ3JpZHN0YWNrXCI7XHJcbmltcG9ydCB7IEdyaWRzdGFja0NvbXBvbmVudCwgZ3NDcmVhdGVOZ0NvbXBvbmVudHMsIGdzU2F2ZUFkZGl0aW9uYWxOZ0luZm8gfSBmcm9tIFwiLi9ncmlkc3RhY2suY29tcG9uZW50XCI7XHJcbmltcG9ydCB7IEdyaWRzdGFja0l0ZW1Db21wb25lbnQgfSBmcm9tIFwiLi9ncmlkc3RhY2staXRlbS5jb21wb25lbnRcIjtcclxuXHJcbkBOZ01vZHVsZSh7XHJcbiAgaW1wb3J0czogW1xyXG4gICAgQ29tbW9uTW9kdWxlLFxyXG4gIF0sXHJcbiAgZGVjbGFyYXRpb25zOiBbXHJcbiAgICBHcmlkc3RhY2tDb21wb25lbnQsXHJcbiAgICBHcmlkc3RhY2tJdGVtQ29tcG9uZW50LFxyXG4gIF0sXHJcbiAgZXhwb3J0czogW1xyXG4gICAgR3JpZHN0YWNrQ29tcG9uZW50LFxyXG4gICAgR3JpZHN0YWNrSXRlbUNvbXBvbmVudCxcclxuICBdLFxyXG59KVxyXG5leHBvcnQgY2xhc3MgR3JpZHN0YWNrTW9kdWxlIHtcclxuICBjb25zdHJ1Y3RvcigpIHtcclxuICAgIC8vIHNldCBnbG9iYWxseSBvdXIgbWV0aG9kIHRvIGNyZWF0ZSB0aGUgcmlnaHQgd2lkZ2V0IHR5cGVcclxuICAgIEdyaWRTdGFjay5hZGRSZW1vdmVDQiA9IGdzQ3JlYXRlTmdDb21wb25lbnRzO1xyXG4gICAgR3JpZFN0YWNrLnNhdmVDQiA9IGdzU2F2ZUFkZGl0aW9uYWxOZ0luZm87XHJcbiAgfVxyXG59XHJcbiJdfQ==