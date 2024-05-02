/**
 * gridstack-item.component.ts 8.2.3
 * Copyright (c) 2022 Alain Dumesny - see GridStack root license
 */
import { Component, Input, ViewChild, ViewContainerRef } from '@angular/core';
import * as i0 from "@angular/core";
/**
 * HTML Component Wrapper for gridstack items, in combination with GridstackComponent for parent grid
 */
export class GridstackItemComponent {
    constructor(elementRef) {
        this.elementRef = elementRef;
        this.el._gridItemComp = this;
    }
    /** list of options for creating/updating this item */
    set options(val) {
        if (this.el.gridstackNode?.grid) {
            // already built, do an update...
            this.el.gridstackNode.grid.update(this.el, val);
        }
        else {
            // store our custom element in options so we can update it and not re-create a generic div!
            this._options = { ...val, el: this.el };
        }
    }
    /** return the latest grid options (from GS once built, otherwise initial values) */
    get options() {
        return this.el.gridstackNode || this._options || { el: this.el };
    }
    /** return the native element that contains grid specific fields as well */
    get el() { return this.elementRef.nativeElement; }
    /** clears the initial options now that we've built */
    clearOptions() {
        delete this._options;
    }
    ngOnDestroy() {
        delete this.ref;
        delete this.el._gridItemComp;
    }
}
GridstackItemComponent.ɵfac = i0.ɵɵngDeclareFactory({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: GridstackItemComponent, deps: [{ token: i0.ElementRef }], target: i0.ɵɵFactoryTarget.Component });
GridstackItemComponent.ɵcmp = i0.ɵɵngDeclareComponent({ minVersion: "14.0.0", version: "14.3.0", type: GridstackItemComponent, selector: "gridstack-item", inputs: { options: "options" }, viewQueries: [{ propertyName: "container", first: true, predicate: ["container"], descendants: true, read: ViewContainerRef, static: true }], ngImport: i0, template: `
    <div class="grid-stack-item-content">
      <!-- where dynamic items go based on component types, or sub-grids, etc...) -->
      <ng-template #container></ng-template>
      <!-- any static (defined in dom) content goes here -->
      <ng-content></ng-content>
      <!-- fallback HTML content from GridStackWidget content field if used instead -->
      {{options.content}}
    </div>`, isInline: true, styles: [":host{display:block}\n"] });
i0.ɵɵngDeclareClassMetadata({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: GridstackItemComponent, decorators: [{
            type: Component,
            args: [{ selector: 'gridstack-item', template: `
    <div class="grid-stack-item-content">
      <!-- where dynamic items go based on component types, or sub-grids, etc...) -->
      <ng-template #container></ng-template>
      <!-- any static (defined in dom) content goes here -->
      <ng-content></ng-content>
      <!-- fallback HTML content from GridStackWidget content field if used instead -->
      {{options.content}}
    </div>`, styles: [":host{display:block}\n"] }]
        }], ctorParameters: function () { return [{ type: i0.ElementRef }]; }, propDecorators: { container: [{
                type: ViewChild,
                args: ['container', { read: ViewContainerRef, static: true }]
            }], options: [{
                type: Input
            }] } });
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZ3JpZHN0YWNrLWl0ZW0uY29tcG9uZW50LmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vLi4vLi4vLi4vYW5ndWxhci9wcm9qZWN0cy9saWIvc3JjL2xpYi9ncmlkc3RhY2staXRlbS5jb21wb25lbnQudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OztHQUdHO0FBRUgsT0FBTyxFQUFFLFNBQVMsRUFBYyxLQUFLLEVBQUUsU0FBUyxFQUFFLGdCQUFnQixFQUEyQixNQUFNLGVBQWUsQ0FBQzs7QUFTbkg7O0dBRUc7QUFpQkgsTUFBTSxPQUFPLHNCQUFzQjtJQW9DakMsWUFBNkIsVUFBMkM7UUFBM0MsZUFBVSxHQUFWLFVBQVUsQ0FBaUM7UUFDdEUsSUFBSSxDQUFDLEVBQUUsQ0FBQyxhQUFhLEdBQUcsSUFBSSxDQUFDO0lBQy9CLENBQUM7SUEzQkQsc0RBQXNEO0lBQ3RELElBQW9CLE9BQU8sQ0FBQyxHQUFrQjtRQUM1QyxJQUFJLElBQUksQ0FBQyxFQUFFLENBQUMsYUFBYSxFQUFFLElBQUksRUFBRTtZQUMvQixpQ0FBaUM7WUFDakMsSUFBSSxDQUFDLEVBQUUsQ0FBQyxhQUFhLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxJQUFJLENBQUMsRUFBRSxFQUFFLEdBQUcsQ0FBQyxDQUFDO1NBQ2pEO2FBQU07WUFDTCwyRkFBMkY7WUFDM0YsSUFBSSxDQUFDLFFBQVEsR0FBRyxFQUFDLEdBQUcsR0FBRyxFQUFFLEVBQUUsRUFBRSxJQUFJLENBQUMsRUFBRSxFQUFDLENBQUM7U0FDdkM7SUFDSCxDQUFDO0lBQ0Qsb0ZBQW9GO0lBQ3BGLElBQVcsT0FBTztRQUNoQixPQUFPLElBQUksQ0FBQyxFQUFFLENBQUMsYUFBYSxJQUFJLElBQUksQ0FBQyxRQUFRLElBQUksRUFBQyxFQUFFLEVBQUUsSUFBSSxDQUFDLEVBQUUsRUFBQyxDQUFDO0lBQ2pFLENBQUM7SUFJRCwyRUFBMkU7SUFDM0UsSUFBVyxFQUFFLEtBQThCLE9BQU8sSUFBSSxDQUFDLFVBQVUsQ0FBQyxhQUFhLENBQUMsQ0FBQyxDQUFDO0lBRWxGLHNEQUFzRDtJQUMvQyxZQUFZO1FBQ2pCLE9BQU8sSUFBSSxDQUFDLFFBQVEsQ0FBQztJQUN2QixDQUFDO0lBTU0sV0FBVztRQUNoQixPQUFPLElBQUksQ0FBQyxHQUFHLENBQUM7UUFDaEIsT0FBTyxJQUFJLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQztJQUMvQixDQUFDOzttSEEzQ1Usc0JBQXNCO3VHQUF0QixzQkFBc0IseUtBR0QsZ0JBQWdCLDJDQWpCdEM7Ozs7Ozs7O1dBUUQ7MkZBTUUsc0JBQXNCO2tCQWhCbEMsU0FBUzsrQkFDRSxnQkFBZ0IsWUFDaEI7Ozs7Ozs7O1dBUUQ7aUdBUytELFNBQVM7c0JBQWhGLFNBQVM7dUJBQUMsV0FBVyxFQUFFLEVBQUUsSUFBSSxFQUFFLGdCQUFnQixFQUFFLE1BQU0sRUFBRSxJQUFJLEVBQUM7Z0JBUzNDLE9BQU87c0JBQTFCLEtBQUsiLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIGdyaWRzdGFjay1pdGVtLmNvbXBvbmVudC50cyA4LjIuM1xuICogQ29weXJpZ2h0IChjKSAyMDIyIEFsYWluIER1bWVzbnkgLSBzZWUgR3JpZFN0YWNrIHJvb3QgbGljZW5zZVxuICovXG5cbmltcG9ydCB7IENvbXBvbmVudCwgRWxlbWVudFJlZiwgSW5wdXQsIFZpZXdDaGlsZCwgVmlld0NvbnRhaW5lclJlZiwgT25EZXN0cm95LCBDb21wb25lbnRSZWYgfSBmcm9tICdAYW5ndWxhci9jb3JlJztcbmltcG9ydCB7IEdyaWRJdGVtSFRNTEVsZW1lbnQsIEdyaWRTdGFja05vZGUgfSBmcm9tICdncmlkc3RhY2snO1xuaW1wb3J0IHsgQmFzZVdpZGdldCB9IGZyb20gJy4vYmFzZS13aWRnZXQnO1xuXG4vKiogc3RvcmUgZWxlbWVudCB0byBOZyBDbGFzcyBwb2ludGVyIGJhY2sgKi9cbmV4cG9ydCBpbnRlcmZhY2UgR3JpZEl0ZW1Db21wSFRNTEVsZW1lbnQgZXh0ZW5kcyBHcmlkSXRlbUhUTUxFbGVtZW50IHtcbiAgX2dyaWRJdGVtQ29tcD86IEdyaWRzdGFja0l0ZW1Db21wb25lbnQ7XG59XG5cbi8qKlxuICogSFRNTCBDb21wb25lbnQgV3JhcHBlciBmb3IgZ3JpZHN0YWNrIGl0ZW1zLCBpbiBjb21iaW5hdGlvbiB3aXRoIEdyaWRzdGFja0NvbXBvbmVudCBmb3IgcGFyZW50IGdyaWRcbiAqL1xuQENvbXBvbmVudCh7XG4gIHNlbGVjdG9yOiAnZ3JpZHN0YWNrLWl0ZW0nLFxuICB0ZW1wbGF0ZTogYFxuICAgIDxkaXYgY2xhc3M9XCJncmlkLXN0YWNrLWl0ZW0tY29udGVudFwiPlxuICAgICAgPCEtLSB3aGVyZSBkeW5hbWljIGl0ZW1zIGdvIGJhc2VkIG9uIGNvbXBvbmVudCB0eXBlcywgb3Igc3ViLWdyaWRzLCBldGMuLi4pIC0tPlxuICAgICAgPG5nLXRlbXBsYXRlICNjb250YWluZXI+PC9uZy10ZW1wbGF0ZT5cbiAgICAgIDwhLS0gYW55IHN0YXRpYyAoZGVmaW5lZCBpbiBkb20pIGNvbnRlbnQgZ29lcyBoZXJlIC0tPlxuICAgICAgPG5nLWNvbnRlbnQ+PC9uZy1jb250ZW50PlxuICAgICAgPCEtLSBmYWxsYmFjayBIVE1MIGNvbnRlbnQgZnJvbSBHcmlkU3RhY2tXaWRnZXQgY29udGVudCBmaWVsZCBpZiB1c2VkIGluc3RlYWQgLS0+XG4gICAgICB7e29wdGlvbnMuY29udGVudH19XG4gICAgPC9kaXY+YCxcbiAgc3R5bGVzOiBbYFxuICAgIDpob3N0IHsgZGlzcGxheTogYmxvY2s7IH1cbiAgYF0sXG4gIC8vIGNoYW5nZURldGVjdGlvbjogQ2hhbmdlRGV0ZWN0aW9uU3RyYXRlZ3kuT25QdXNoLCAvLyBJRkYgeW91IHdhbnQgdG8gb3B0aW1pemUgYW5kIGNvbnRyb2wgd2hlbiBDaGFuZ2VEZXRlY3Rpb24gbmVlZHMgdG8gaGFwcGVuLi4uXG59KVxuZXhwb3J0IGNsYXNzIEdyaWRzdGFja0l0ZW1Db21wb25lbnQgaW1wbGVtZW50cyBPbkRlc3Ryb3kge1xuXG4gIC8qKiBjb250YWluZXIgdG8gYXBwZW5kIGl0ZW1zIGR5bmFtaWNhbGx5ICovXG4gIEBWaWV3Q2hpbGQoJ2NvbnRhaW5lcicsIHsgcmVhZDogVmlld0NvbnRhaW5lclJlZiwgc3RhdGljOiB0cnVlfSkgcHVibGljIGNvbnRhaW5lcj86IFZpZXdDb250YWluZXJSZWY7XG5cbiAgLyoqIENvbXBvbmVudFJlZiBvZiBvdXJzZWxmIC0gdXNlZCBieSBkeW5hbWljIG9iamVjdCB0byBjb3JyZWN0bHkgZ2V0IHJlbW92ZWQgKi9cbiAgcHVibGljIHJlZjogQ29tcG9uZW50UmVmPEdyaWRzdGFja0l0ZW1Db21wb25lbnQ+IHwgdW5kZWZpbmVkO1xuXG4gIC8qKiBjaGlsZCBjb21wb25lbnQgc28gd2UgY2FuIHNhdmUvcmVzdG9yZSBhZGRpdGlvbmFsIGRhdGEgdG8gYmUgc2F2ZWQgYWxvbmcgKi9cbiAgcHVibGljIGNoaWxkV2lkZ2V0OiBCYXNlV2lkZ2V0IHwgdW5kZWZpbmVkO1xuXG4gIC8qKiBsaXN0IG9mIG9wdGlvbnMgZm9yIGNyZWF0aW5nL3VwZGF0aW5nIHRoaXMgaXRlbSAqL1xuICBASW5wdXQoKSBwdWJsaWMgc2V0IG9wdGlvbnModmFsOiBHcmlkU3RhY2tOb2RlKSB7XG4gICAgaWYgKHRoaXMuZWwuZ3JpZHN0YWNrTm9kZT8uZ3JpZCkge1xuICAgICAgLy8gYWxyZWFkeSBidWlsdCwgZG8gYW4gdXBkYXRlLi4uXG4gICAgICB0aGlzLmVsLmdyaWRzdGFja05vZGUuZ3JpZC51cGRhdGUodGhpcy5lbCwgdmFsKTtcbiAgICB9IGVsc2Uge1xuICAgICAgLy8gc3RvcmUgb3VyIGN1c3RvbSBlbGVtZW50IGluIG9wdGlvbnMgc28gd2UgY2FuIHVwZGF0ZSBpdCBhbmQgbm90IHJlLWNyZWF0ZSBhIGdlbmVyaWMgZGl2IVxuICAgICAgdGhpcy5fb3B0aW9ucyA9IHsuLi52YWwsIGVsOiB0aGlzLmVsfTtcbiAgICB9XG4gIH1cbiAgLyoqIHJldHVybiB0aGUgbGF0ZXN0IGdyaWQgb3B0aW9ucyAoZnJvbSBHUyBvbmNlIGJ1aWx0LCBvdGhlcndpc2UgaW5pdGlhbCB2YWx1ZXMpICovXG4gIHB1YmxpYyBnZXQgb3B0aW9ucygpOiBHcmlkU3RhY2tOb2RlIHtcbiAgICByZXR1cm4gdGhpcy5lbC5ncmlkc3RhY2tOb2RlIHx8IHRoaXMuX29wdGlvbnMgfHwge2VsOiB0aGlzLmVsfTtcbiAgfVxuXG4gIHByaXZhdGUgX29wdGlvbnM/OiBHcmlkU3RhY2tOb2RlO1xuXG4gIC8qKiByZXR1cm4gdGhlIG5hdGl2ZSBlbGVtZW50IHRoYXQgY29udGFpbnMgZ3JpZCBzcGVjaWZpYyBmaWVsZHMgYXMgd2VsbCAqL1xuICBwdWJsaWMgZ2V0IGVsKCk6IEdyaWRJdGVtQ29tcEhUTUxFbGVtZW50IHsgcmV0dXJuIHRoaXMuZWxlbWVudFJlZi5uYXRpdmVFbGVtZW50OyB9XG5cbiAgLyoqIGNsZWFycyB0aGUgaW5pdGlhbCBvcHRpb25zIG5vdyB0aGF0IHdlJ3ZlIGJ1aWx0ICovXG4gIHB1YmxpYyBjbGVhck9wdGlvbnMoKSB7XG4gICAgZGVsZXRlIHRoaXMuX29wdGlvbnM7XG4gIH1cblxuICBjb25zdHJ1Y3Rvcihwcml2YXRlIHJlYWRvbmx5IGVsZW1lbnRSZWY6IEVsZW1lbnRSZWY8R3JpZEl0ZW1IVE1MRWxlbWVudD4pIHtcbiAgICB0aGlzLmVsLl9ncmlkSXRlbUNvbXAgPSB0aGlzO1xuICB9XG5cbiAgcHVibGljIG5nT25EZXN0cm95KCk6IHZvaWQge1xuICAgIGRlbGV0ZSB0aGlzLnJlZjtcbiAgICBkZWxldGUgdGhpcy5lbC5fZ3JpZEl0ZW1Db21wO1xuICB9XG59XG4iXX0=