class Solution {
public:
    int search(vector<int>& nums, int target) {
        int sie=nums.size();
        int start=0,end=sie-1;
        while(start<=end){
            int mid=(start+end)/2;
            if(target==nums[mid]){
                return mid;
            }
            else if(target>nums[mid]){
                start=mid+1;
            }
            else{
                end=mid-1;
            }
        }
        return -1;
    }
};
