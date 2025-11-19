#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
       int maxCount = 0;
        for(string s : sentences){
            int count = 0;
            for(int i = 0; i < s.size(); i++){
                if(s.at(i) == ' '){
                    count++;
                }
            }
            maxCount = max(maxCount,count+1);
        }
        return maxCount;

    }
};

// Test function
void runTests() {
    Solution solution;
    
    // Test case 1: Basic example
    vector<string> sentences1 = {"alice and bob love leetcode", "i think so too", "this is great thanks very much"};
    int result1 = solution.mostWordsFound(sentences1);
    cout << "Test 1: ";
    for(const string& s : sentences1) cout << "\"" << s << "\" ";
    cout << "\nResult: " << result1 << "\n\n";
    
    // Test case 2: Single word sentences
    vector<string> sentences2 = {"hello", "world", "cpp"};
    int result2 = solution.mostWordsFound(sentences2);
    cout << "Test 2: ";
    for(const string& s : sentences2) cout << "\"" << s << "\" ";
    cout << "\nResult: " << result2 << "\n\n";
    
    // Test case 3: One sentence with many words
    vector<string> sentences3 = {"this sentence has many words in it", "short", "ok"};
    int result3 = solution.mostWordsFound(sentences3);
    cout << "Test 3: ";
    for(const string& s : sentences3) cout << "\"" << s << "\" ";
    cout << "\nResult: " << result3 << "\n\n";
    
    // Test case 4: Empty spaces and punctuation
    vector<string> sentences4 = {"hello world!", "this is a test", "a", "multiple spaces  here"};
    int result4 = solution.mostWordsFound(sentences4);
    cout << "Test 4: ";
    for(const string& s : sentences4) cout << "\"" << s << "\" ";
    cout << "\nResult: " << result4 << "\n\n";
    
    // Test case 5: Single sentence
    vector<string> sentences5 = {"only one sentence with several words"};
    int result5 = solution.mostWordsFound(sentences5);
    cout << "Test 5: ";
    for(const string& s : sentences5) cout << "\"" << s << "\" ";
    cout << "\nResult: " << result5 << "\n\n";
}

int main() {
    cout << "Running tests for mostWordsFound function:\n\n";
    runTests();
    return 0;
}